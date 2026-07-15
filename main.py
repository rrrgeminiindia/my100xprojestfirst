import gradio as gr
import requests


RENDER_API_URL = "https://my100xprojestfirst.onrender.com/diagnose"


def diagnose(workflow_description):
    if not workflow_description.strip():
        return "Please enter a workflow description."

    try:
        response = requests.post(
            RENDER_API_URL,
            json={
                "workflow_description": workflow_description
            },
            timeout=120
        )

        response.raise_for_status()
        data = response.json()

        return data.get(
            "diagnosis",
            "The backend did not return a diagnosis."
        )

    except requests.exceptions.Timeout:
        return "The Render backend took too long to respond."

    except requests.exceptions.RequestException as error:
        return f"Backend request failed: {error}"


demo = gr.Interface(
    fn=diagnose,
    inputs=gr.Textbox(
        label="Workflow Description",
        placeholder="Describe the workflow you want to automate...",
        lines=8
    ),
    outputs=gr.Markdown(
        label="Automation Diagnosis Plan"
    ),
    title="Automation Diagnosis Tool"
)


if __name__ == "__main__":
    demo.launch()
