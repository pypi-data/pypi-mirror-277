#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <pyaccell/engine.hpp>
#include <pyaccell/shader.hpp>
#include <pyaccell/rules.hpp>

#include <iostream>

void framebuffer_size_callback(GLFWwindow* window, int width, int height);
void processInput(GLFWwindow *window);

// settings
int scr_width = 800;
int scr_height = 600;
const unsigned int FRAME_WIDTH = 800;
const unsigned int FRAME_HEIGHT = 600;

int pyaccell::run(const unsigned int* rule, const unsigned int states)
{
    glfwInit();
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

#ifdef __APPLE__
    glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);
#endif

    GLFWwindow* window = glfwCreateWindow(scr_width, scr_height, "Pyaccell", NULL, NULL);
    if (window == NULL)
    {
        std::cout << "Failed to create GLFW window" << std::endl;
        glfwTerminate();
        return -1;
    }
    glfwMakeContextCurrent(window);
    glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);
    // this is necessary for high resolution displays otherwise only part of window is rendered
    glfwGetFramebufferSize(window, &scr_width, &scr_height);

    // glad: load all OpenGL function pointers
    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress))
    {
        std::cout << "Failed to initialize GLAD" << std::endl;
        return -1;
    }
    glViewport(0, 0, scr_width, scr_height);

    pyaccell::Shader screenShader(SHADER_PATH "framebuffers_screen.vs", SHADER_PATH "framebuffers_screen.fs");
    pyaccell::Shader simShader(SHADER_PATH "sim.vs", SHADER_PATH "sim.fs");

    // vertex attributes for a quad that fills the entire screen in Normalized Device Coordinates.
    float quadVertices[] = { 
        // positions   // texCoords
        -1.0f,  1.0f,  0.0f, 1.0f,
        -1.0f, -1.0f,  0.0f, 0.0f,
         1.0f, -1.0f,  1.0f, 0.0f,

        -1.0f,  1.0f,  0.0f, 1.0f,
         1.0f, -1.0f,  1.0f, 0.0f,
         1.0f,  1.0f,  1.0f, 1.0f
    };
    // screen quad VAO
    unsigned int quadVAO, quadVBO;
    glGenVertexArrays(1, &quadVAO);
    glGenBuffers(1, &quadVBO);
    glBindVertexArray(quadVAO);
    glBindBuffer(GL_ARRAY_BUFFER, quadVBO);
    glBufferData(GL_ARRAY_BUFFER, sizeof(quadVertices), &quadVertices, GL_STATIC_DRAW);
    glEnableVertexAttribArray(0);
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 4 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(1);
    glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 4 * sizeof(float), (void*)(2 * sizeof(float)));
    glBindVertexArray(0);
    // final screen shader configuration
    screenShader.use();
    screenShader.setInt("screenTexture", 0);

    // framebuffer configuration
    // -------------------------
    /**
        framebuffer(textureInput) -> textureOutput
        framebuffer_alt(textureOutput) -> textureInput
        swap or alternate framebuffers each loop
    */
    unsigned int framebuffer[2];
    unsigned int textureInput[2];
    unsigned int textureColorbuffer = pyaccell::create_color_texture(FRAME_WIDTH, FRAME_HEIGHT);
    glGenTextures(2, textureInput);
    glGenFramebuffers(2, framebuffer);
    for (int i=0; i<2; i++) {
        glBindFramebuffer(GL_FRAMEBUFFER, framebuffer[i]);
        if (i == 0) {
            textureInput[i] = pyaccell::random_input_state(FRAME_WIDTH, FRAME_HEIGHT, 2);
        }
        else {
            textureInput[i] = pyaccell::create_empty_texture(FRAME_WIDTH, FRAME_HEIGHT);
        }
        glBindTexture(GL_TEXTURE_2D, textureColorbuffer);
        glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, textureColorbuffer, 0);
        glBindTexture(GL_TEXTURE_2D, textureInput[i]);
        glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT1, GL_TEXTURE_2D, textureInput[i], 0);
        if (glCheckFramebufferStatus(GL_FRAMEBUFFER) != GL_FRAMEBUFFER_COMPLETE)
            std::cout << "ERROR::FRAMEBUFFER:: Framebuffer is not complete!" << std::endl;
        glBindFramebuffer(GL_FRAMEBUFFER, 0);
    }
    GLenum framebufs[2] = {GL_COLOR_ATTACHMENT0, GL_COLOR_ATTACHMENT1};

    // simShader uniforms
    unsigned int textureBinomials = pyaccell::generate_binomials();
    unsigned int indices = pyaccell::no_of_indices(states);
    unsigned int textureRule = pyaccell::generate_rule(rule, indices, states);
    enum SAMPLER {BINOMIAL = 1, INPUT = 2, RULE = 3};
    simShader.use();
    simShader.setInt("uBinomial", BINOMIAL);
    simShader.setInt("inputStates", INPUT);
    simShader.setInt("rule", RULE);
    simShader.setInt("numStates", states);
    simShader.setInt("inputWidth", FRAME_WIDTH);
    simShader.setInt("inputHeight", FRAME_HEIGHT);

    int input_index = 0;
    // render loop
    while (!glfwWindowShouldClose(window))
    {
        // input
        processInput(window);
        int output_index = (input_index == 0) ? 1 : 0;

        // render
        /*bind to framebuffer alternatively and "draw" to textureInput
            start with frame_index=0 as input and frame_index=1(alt_index) as output
        */
        glViewport(0, 0, FRAME_WIDTH, FRAME_HEIGHT);
        glBindFramebuffer(GL_FRAMEBUFFER, framebuffer[output_index]);
        glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);
        glDrawBuffers(2, framebufs);
        simShader.use();
        glBindVertexArray(quadVAO);
        glActiveTexture(GL_TEXTURE0 + BINOMIAL);
        glBindTexture(GL_TEXTURE_2D, textureBinomials);
        glActiveTexture(GL_TEXTURE0 + RULE);
        glBindTexture(GL_TEXTURE_2D, textureRule);
        glActiveTexture(GL_TEXTURE0 + INPUT);
        glBindTexture(GL_TEXTURE_2D, textureInput[input_index]);
        glDrawArrays(GL_TRIANGLES, 0, 6);

        // now bind back to default framebuffer and draw a quad plane with the attached framebuffer color texture
        glViewport(0, 0, scr_width, scr_height);
        glBindFramebuffer(GL_FRAMEBUFFER, 0);
        glDisable(GL_DEPTH_TEST); // disable depth test so screen-space quad isn't discarded due to depth test.
        glClearColor(1.0f, 1.0f, 1.0f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);

        screenShader.use();
        glBindVertexArray(quadVAO);
        glActiveTexture(GL_TEXTURE0);
        glBindTexture(GL_TEXTURE_2D, textureColorbuffer);
        glDrawArrays(GL_TRIANGLES, 0, 6);

        // glfw: swap buffers and poll IO events (keys pressed/released, mouse moved etc.)
        input_index = output_index;
        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    glfwTerminate();
    return 0;
}

// process all input: query GLFW whether relevant keys are pressed/released this frame and react accordingly
void processInput(GLFWwindow *window)
{
    if(glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
        glfwSetWindowShouldClose(window, true);
}

// glfw: whenever the window size changed (by OS or user resize) this callback function executes
void framebuffer_size_callback(GLFWwindow* window, int width, int height)
{
    // make sure the viewport matches the new window dimensions; note that width and 
    // height will be significantly larger than specified on retina displays.
    //glViewport(0, 0, width, height);
    scr_width = width;
    scr_height = height;
}