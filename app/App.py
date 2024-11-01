import gradio as gr
  
with gr.Blocks() as demo:
    gr.Markdown("""
                <center> 
                <span style='font-size: 50px; font-weight: Bold; font-family: "Noto Serif Sinhala", serif'>
                ශ්‍රී ලංකා ආණ්ඩුක්‍රම ව්‍යවස්ථාව QnA 
                </span>
                </center>
                """)
    
    with gr.Row():
        # with gr.Column():
        question = gr.Textbox(label="Question")
            
        # with gr.Column():
        answer = gr.Textbox(label="Answer")
    
    summarize_btn = gr.Button(value="Generate", size = 'sm')

demo.launch(inbrowser=True)
