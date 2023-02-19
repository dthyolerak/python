from web import create_app #importing create app from web fold

app = create_app() 

if __name__ == '__main__': #run this flask app only if file is main
    app.run(debug=True) #to run automatic once you change code // turn it off  in production