from flask import Flask, render_template_string, request   # Importing the Flask modules required for this project
from time import sleep      # Import sleep module from time library to add delays
import serial

# Flask constructor takes the name of current module (__name__) as argument.
app = Flask(__name__)
# Enable debug mode
app.config['DEBUG'] = True
 
# Store HTML code
TPL = '''
<html>
    <head>
        <title>Web Application to control Servos </title>
        
        <style>
            body{
                background: #b92b27;  /* fallback for old browsers */
                background: -webkit-linear-gradient(to right, #1565C0, #b92b27);  /* Chrome 10-25, Safari 5.1-6 */
                background: linear-gradient(to right, #1565C0, #b92b27); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
            }
            .enviar{
                color: blue;
                float: right;
            }
        </style>
    </head>
    <body>
    <h2> Web Application to Control Servos</h2>
        <form method="POST" action="test">
        
            <p>Mover Brazo(Grados)<input type="range" min="0" max="180" step="1" value="90" name="slider1"><label>90</label></p>
            
            Agarrar<input type="radio" name="pinza" value="agarrar" />
            Soltar<input type="radio" name="pinza" value="soltar" checked /> 
            <input class="enviar" type="submit" value="Submit" />
        </form>
        
        <script>
        var input = document.querySelector("input[type=range]");
           actualizarInput(input) 


        input.addEventListener("input", function(evt) {
           actualizarInput(input)
        });

        function actualizarInput(input){
           var label = input.parentElement.querySelector("label");
           label.innerHTML = input.value;
           var inputMin = input.getAttribute("min");
           var inputMax = input.getAttribute("max");
           var unidad = (inputMax - inputMin) / 100;
           input.style.setProperty("--value", (input.value - inputMin)/unidad);  
        }
        
        
        </script>
    </body>
</html>
'''
 
# which URL should call the associated function.
@app.route("/")
def home():
    return render_template_string(TPL)
 
@app.route("/test", methods=["POST"])
def test():
    s = serial.Serial("/dev/ttyACM0",9600)
    
    # Get slider Values
    slider1 = request.form["slider1"]
    opcion = request.form["pinza"]
    
    #Use values
    print(slider1,' grados')
    print('opcion ',opcion)
    
    s.write(slider1.encode())
    
    sleep(2)
    s.write(opcion.encode())
    
    
    return render_template_string(TPL)
 
# Run the app on the local development server
if __name__ == "__main__":
    app.run()