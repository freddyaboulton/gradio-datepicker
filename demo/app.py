
import gradio as gr
from gradio_datepicker import DatePicker


example = DatePicker().example_inputs()

demo = gr.Interface(
    lambda x:x,
    DatePicker(),  # interactive version of your component
    DatePicker(),  # static version of your component
    # examples=[[example]],  # uncomment this line to view the "example version" of your component
)


demo.launch()
