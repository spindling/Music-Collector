# main.py
# - Setups up the model, view, and controller objects through
#   mvc.py and starts the application. 
import mvc

def main():
    model = mvc.Model()
    view = mvc.View()
    controller = mvc.Controller(model, view)
    controller.start()
        
if __name__=="__main__":
    main()