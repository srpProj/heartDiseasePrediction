from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///genome.db"
db = SQLAlchemy(app)
class Data(db.Model):
    id=db.Column(db.Integer,primary_key=True,default="2722")
    name=db.Column(db.String(200),nullable=False,default="Ajay")
    age=db.Column(db.Integer,nullable=False,default="20")
    sex=db.Column(db.String(200),nullable=False)
    cp=db.Column(db.String(200),nullable=False)
    trestbps=db.Column(db.String(200),nullable=False)
    thalach=db.Column(db.String(200),nullable=False)
    chol=db.Column(db.String(200),nullable=False)
    fbs=db.Column(db.String(200),nullable=False)
    resetecg=db.Column(db.String(200),nullable=False)
    exang=db.Column(db.String(200),nullable=False)
    oldpeak=db.Column(db.String(200),nullable=False)
    slope=db.Column(db.String(200),nullable=False)
    ca=db.Column(db.String(200),nullable=False)
    thal=db.Column(db.String(200),nullable=False)
    num=db.Column(db.String(200),nullable=False)
    def __init__(self,id,name,age,sex,cp,trestbps,thalach,chol,fbs,resetecg,exang,oldpeak,slope,ca,thal,num):
        self.id=id
        self.name=name
        self.age=age
        self.sex=sex
        self.cp=cp
        self.trestbps=trestbps
        self.thalach=thalach
        self.chol=chol
        self.fbs=fbs
        self.resetecg=resetecg
        self.exang=exang
        self.oldpeak=oldpeak
        self.slope=slope
        self.ca=ca
        self.thal=thal
        self.num=num
@app.route("/",methods=["POST","GET"])
def index():
    if request.method == "POST":
        p_id=request.form["id"]
        p_name=request.form["name"]
        p_age=request.form["age"]
        p_sex = request.form["sex"]
        p_cp = request.form["cp"]
        p_trestbps= request.form["trestbps"]
        p_thalach= request.form["thalach"]
        p_chol= request.form["chol"]
        p_fbs= request.form["fbs"]
        p_resetecg= request.form["resetecg"]
        p_exang= request.form["exang"]
        p_oldpeak= request.form["oldpeak"]
        p_slope= request.form["slope"]
        p_ca= request.form["ca"]
        p_thal= request.form["thal"]
        p_num= request.form["num"]
        obj=Data(p_id,p_name,p_age,p_sex,p_cp,p_trestbps,p_thalach,p_chol,p_fbs,p_resetecg,p_exang,p_oldpeak,p_slope,p_ca,p_thal,p_num)
        try:
            db.session.add(obj)
            db.session.commit()
            return redirect("/")
        except:
            return "Dont worry Its Fixed"
    else: 
        tasks = Data.query.order_by(Data.id).all()
        return render_template("index.html", tasks=tasks)
@app.route("/delete/<int:id>")
def delete(id):
    task_to_delete=Data.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "delete error"
@app.route("/update/<int:id>",methods=["GET","POST"])
def update(id):
    task=Data.query.get_or_404(id)
    if request.method == "POST":
        task.name=request.form["name"]
        task.age=request.form["age"]
        task.sex = request.form["sex"]
        task.cp= request.form["cp"]
        task.trestbps= request.form["trestbps"]
        task.thalach= request.form["thalach"]
        task.chol= request.form["chol"]
        task.fbs= request.form["fbs"]
        task.resetecg= request.form["resetecg"]
        task.exang= request.form["exang"]
        task.oldpeak= request.form["oldpeak"]
        task.slope= request.form["slope"]
        task.ca= request.form["ca"]
        task.thal= request.form["thal"]
        task.num= request.form["num"]
        try:
            db.session.commit()
            return redirect("/")
        except:
            return "Update error"
        #return "In POST"
        return redirect("/")
    else:
        #return "In GET"
        return render_template("update.html",task=task)
if __name__=="__main__":
    app.run(debug=True)