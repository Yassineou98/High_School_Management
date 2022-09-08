from project.__init__ import db
from project.models import User, Marks

from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from flask_login import current_user, login_required

main = Blueprint('main', __name__)


@main.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('index.html', name=current_user.name_teacher)
    else:
        return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name_teacher)


@main.route('/enseig_profile')
@login_required
def enseig_profile():
    return render_template('enseig_profil.html', name=current_user.name_teacher, email=current_user.email)


@main.route("/new")
@login_required
def new_student():
    return render_template('add_student_mark.html', name=current_user.name_teacher)


@main.route("/new", methods=['POST'])
@login_required
def new_student_post():
    specialite = request.form.get('specialite')

    if not (specialite == 'IDL' or specialite == 'Reseau' or specialite == 'SE'):
        flash('Veuillez vérifier vos informations et réessayer.')
        return redirect(url_for('main.new_student_post'))

    if specialite == 'IDL':
        return render_template('add_student_idl.html', name=current_user.name_teacher)
    if specialite == 'Reseau':
        return render_template('add_student_rs.html', name=current_user.name_teacher)
    if specialite == 'SE':
        return render_template('add_student_se.html', name=current_user.name_teacher)


@main.route("/new/idl", methods=['POST'])
@login_required
def new_student_idl():
    note = []
    id_student = request.form.get('id_student')
    name = request.form.get('name')
    note.append(request.form.get('note1'))
    note.append(request.form.get('note2'))
    note.append(request.form.get('note3'))
    note.append(request.form.get('note4'))
    note.append(request.form.get('note5'))
    note.append(request.form.get('note6'))
    note.append(request.form.get('note7'))
    note.append(request.form.get('note8'))
    note.append(request.form.get('note9'))
    note.append(request.form.get('note10'))
    note.append(request.form.get('note11'))
    note.append(request.form.get('note12'))
    note.append(request.form.get('note13'))
    note.append(request.form.get('note14'))
    note.append(request.form.get('note15'))
    id_stud = Marks.query.filter_by(id_student=id_student).first()

    if id_stud:
        flash('L"'"ID existe déjà, vérifiez vos informations s"'"il vous plaît.')
        return redirect(url_for('main.new_student_post'))
    print(id_student, name, note)
    student_mark = Marks(id_student=id_student, name=name, specialite='IDL', note1=note[0], note2=note[1],
                         note3=note[2], note4=note[3], note5=note[4], note6=note[5], note7=note[6],
                         note8=note[7], note9=note[8], note10=note[9], note11=note[10], note12=note[11],
                         note13=note[12], note14=note[13], note15=note[14], user_id=current_user.id, notes=note)
    print(Marks.specialite)
    student_mark.calcul_moyenne_idl()
    print(Marks.moyenne_generale_idl)

    print("aa")
    db.session.add(student_mark)
    db.session.commit()
    flash('Etudiant a été ajouté!')
    return redirect(url_for('main.index'))


@main.route("/new/rs", methods=['POST'])
@login_required
def add_student_rs():
    note = []

    id_student = request.form.get('id_student')
    name = request.form.get('name')
    note.append(request.form.get('note1'))
    note.append(request.form.get('note2'))
    note.append(request.form.get('note3'))
    note.append(request.form.get('note4'))
    note.append(request.form.get('note5'))
    note.append(request.form.get('note6'))
    note.append(request.form.get('note7'))
    note.append(request.form.get('note8'))
    note.append(request.form.get('note9'))
    note.append(request.form.get('note10'))
    note.append(request.form.get('note11'))
    note.append(request.form.get('note12'))
    note.append(request.form.get('note13'))
    note.append(request.form.get('note14'))
    note.append(request.form.get('note15'))

    id_stud = Marks.query.filter_by(id_student=id_student).first()

    if id_stud:
        flash('L"'"ID existe déjà, vérifiez vos informations s"'"il vous plaît.')
        return redirect(url_for('main.new_student_post'))

    print(id_student, name, note)
    student_mark = Marks(id_student=id_student, name=name, specialite='Reseau', note1=note[0], note2=note[1],
                         note3=note[2], note4=note[3], note5=note[4], note6=note[5], note7=note[6],
                         note8=note[7], note9=note[8], note10=note[9], note11=note[10], note12=note[11],
                         note13=note[12], note14=note[13], note15=note[14], user_id=current_user.id, notes=note)
    print(Marks.specialite)
    student_mark.calcul_moyenne_rs()
    print(Marks.moyenne_generale_rs)
    print("aa")
    db.session.add(student_mark)
    db.session.commit()
    flash('Etudiant a été ajouté!')
    return redirect(url_for('main.index'))


@main.route("/new/se", methods=['POST'])
@login_required
def new_student_se():
    note = []
    id_student = request.form.get('id_student')
    name = request.form.get('name')
    note.append(request.form.get('note1'))
    note.append(request.form.get('note2'))
    note.append(request.form.get('note3'))
    note.append(request.form.get('note4'))
    note.append(request.form.get('note5'))
    note.append(request.form.get('note6'))
    note.append(request.form.get('note7'))
    note.append(request.form.get('note8'))
    note.append(request.form.get('note9'))
    note.append(request.form.get('note10'))
    note.append(request.form.get('note11'))
    note.append(request.form.get('note12'))
    note.append(request.form.get('note13'))
    note.append(request.form.get('note14'))
    note.append(request.form.get('note15'))
    id_stud = Marks.query.filter_by(id_student=id_student).first()

    if id_stud:
        flash('L"'"ID existe déjà, vérifiez vos informations s"'"il vous plaît.')
        return redirect(url_for('main.new_student_post'))

    print(id_student, name, note)
    student_mark = Marks(id_student=id_student, name=name, specialite='SE', note1=note[0], note2=note[1],
                         note3=note[2], note4=note[3], note5=note[4], note6=note[5], note7=note[6],
                         note8=note[7], note9=note[8], note10=note[9], note11=note[10], note12=note[11],
                         note13=note[12], note14=note[13], note15=note[14], user_id=current_user.id, notes=note)
    student_mark.calcul_moyenne_se()
    print(Marks.moyenne_generale_se)
    print(Marks.specialite)
    print("aa")
    db.session.add(student_mark)
    db.session.commit()
    flash('Etudiant a été ajouté!')
    return redirect(url_for('main.index'))


@main.route("/mark/update2", methods=['POST'])
@login_required
def update_mark2():
    mark = Marks.query.filter_by(id_student=request.form['id']).first()

    mark.note1 = request.form['note1']
    mark.note2 = request.form['note2']
    mark.note3 = request.form['note3']
    mark.note4 = request.form['note4']
    mark.note6 = request.form['note6']
    mark.note7 = request.form['note7']
    mark.note8 = request.form['note8']
    mark.note9 = request.form['note9']
    mark.note10 = request.form['note10']
    mark.note11 = request.form['note11']
    mark.note12 = request.form['note12']
    mark.note13 = request.form['note13']
    mark.note14 = request.form['note14']

    db.session.commit()

    flash('Etudiant a été modifié!')
    return redirect(url_for('main.index'))


@main.route("/mark/update", methods=['POST'])
@login_required
def update_mark():
    print("aaa")
    print(request.form)
    x = request.form['x']
    print(x)
    mark = Marks.query.filter_by(id_student=x).first()
    if not mark:
        flash('Veuillez vérifier vos informations')
        return redirect(url_for('main.profile'))
    print(mark)
    note = [mark.note1, mark.note2, mark.note3, mark.note4, mark.note5, mark.note6, mark.note7, mark.note8, mark.note9,
            mark.note10, mark.note11, mark.note12, mark.note13, mark.note14]

    unite_idl = ['Science des données 1', 'Processus logiciel', 'Systèmes d"informations',
                 'Methodes pour les systèmes complexes', 'Compétences comportementales']
    module_idl = ['Modélisation stochastique', 'Analyse de données', 'Computer vision',
                  'Qualité et test du logiciel', 'Génie logiciel avancé', 'Calcul haute performance',
                  'Conception et programmation', 'Ingénierie des processus', 'Mini-projet',
                  'Dév mobile avancé', 'Mini-projet SE',
                  'Internet marketing', 'Personal development', 'Projet personnel']

    unite_rs = ['Réseaux mobiles', 'Réseaux et sécurité', 'Technologies et protocoles des réseaux étendus',
                'Outils d"evaluation', 'Compétences comportementales']
    module_reseau = ['Réseau radio', 'Réseau sans fil et iot', 'Projet IOT', 'Administration reseau',
                     'Cryptographie avancée',
                     'Communications optiques', 'Réseaux étendus', 'Simulation des reseaux',
                     'Modélisation stochastique',
                     'Dévelopemment des app mobiles', 'Mini-projet dev',
                     'Internet marketing', 'Personal development', 'Projet personnel']

    unite_se = ['Conception et implémentation des circuits numériques', 'Modélisation des systèmes', 'Objects connecté',
                'Sureté des systèmes', 'Compétences comportementales']
    module_se = ['Conception des circuits', 'Mini-projet circuits numérique', 'Modélisation des systèmes',
                 'Commande numérique des systèmes', 'Mini-projet commande numérique', 'Protocoles de communication ',
                 'Capteurs intélligents et reseaux', 'Domotique connectés', 'Sureté de fonctionnement',
                 'Sécurité des SE',
                 'Modélisation stochastique', 'Internet marketing', 'Personal development', 'Projet personnel']

    if mark.specialite == 'IDL':
        return render_template('edit_marks.html', id_student=x, name=mark.name, specialite='IDL',
                               note1=mark.note1, note2=mark.note2,
                               note3=mark.note3, note4=mark.note4, note5=mark.note5, note6=mark.note6,
                               note7=mark.note7,
                               note8=mark.note8, note9=mark.note9, note10=mark.note10, note11=mark.note11,
                               note12=mark.note12,
                               note13=mark.note13, note14=mark.note14, notes=note, unite=unite_idl,
                               text=module_idl)
    if mark.specialite == 'Reseau':
        return render_template('edit_marks.html', id_student=x, name=mark.name, specialite='Reseau',
                               note1=mark.note1, note2=mark.note2,
                               note3=mark.note3, note4=mark.note4, note5=mark.note5, note6=mark.note6, note7=mark.note7,
                               note8=mark.note8, note9=mark.note9, note10=mark.note10, note11=mark.note11,
                               note12=mark.note12,
                               note13=mark.note13, note14=mark.note14, notes=note, unite=unite_rs, text=module_reseau)

    if mark.specialite == 'SE':
        return render_template('edit_marks.html', id_student=x, name=mark.name, specialite='SE',
                               note1=mark.note1, note2=mark.note2,
                               note3=mark.note3, note4=mark.note4, note5=mark.note5, note6=mark.note6, note7=mark.note7,
                               note8=mark.note8, note9=mark.note9, note10=mark.note10, note11=mark.note11,
                               note12=mark.note12,
                               note13=mark.note13, note14=mark.note14, notes=note, unite=unite_se, text=module_se)


@main.route('/mark/check', methods=['POST'])
def check_mark():
    y = request.form['y']
    mark = Marks.query.filter_by(id_student=y).first()

    if not mark:
        flash('Veuillez vérifier vos informations')
        return redirect(url_for('auth.student'))

    note = [mark.note1, mark.note2, mark.note3, mark.note4, mark.note5, mark.note6, mark.note7, mark.note8, mark.note9,
            mark.note10, mark.note11, mark.note12, mark.note13, mark.note14]
    unite_idl = ['Science des données 1', 'Processus logiciel', 'Systèmes d"informations',
                 'Methodes pour les systèmes complexes', 'Compétences comportementales']
    module_idl = ['Modélisation stochastique', 'Analyse de données', 'Computer vision',
                  'Qualité et test du logiciel', 'Génie logiciel avancé', 'Calcul haute performance',
                  'Conception et programmation', 'Ingénierie des processus', 'Mini-projet',
                  'Dév mobile avancé', 'Mini-projet SE',
                  'Internet marketing', 'Personal development', 'Projet personnel']

    unite_rs = ['Réseaux mobiles', 'Réseaux et sécurité', 'Technologies et protocoles des réseaux étendus',
                'Outils d"evaluation', 'Compétences comportementales']
    module_reseau = ['Réseau radio', 'Réseau sans fil et iot', 'Projet IOT', 'Administration reseau',
                     'Cryptographie avancée',
                     'Communications optiques', 'Réseaux étendus', 'Simulation des reseaux',
                     'Modélisation stochastique',
                     'Dévelopemment des app mobiles', 'Mini-projet dev',
                     'Internet marketing', 'Personal development', 'Projet personnel']

    unite_se = ['Conception et implémentation des circuits numériques', 'Modélisation des systèmes', 'Objects connecté',
                'Sureté des systèmes', 'Compétences comportementales']
    module_se = ['Conception des circuits', 'Mini-projet circuits numérique', 'Modélisation des systèmes',
                 'Commande numérique des systèmes', 'Mini-projet commande numérique', 'Protocoles de communication ',
                 'Capteurs intélligents et reseaux', 'Domotique connectés', 'Sureté de fonctionnement',
                 'Sécurité des SE',
                 'Modélisation stochastique', 'Internet marketing', 'Personal development', 'Projet personnel']
    if mark.specialite == 'IDL':
        return render_template('check_mark.html', id_student=y, name=mark.name, specialite=mark.specialite,
                               note1=mark.note1, note2=mark.note2,
                               note3=mark.note3, note4=mark.note4, note5=mark.note5, note6=mark.note6,
                               note7=mark.note7, note8=mark.note8, note9=mark.note9
                               , note10=mark.note10, note11=mark.note11, note12=mark.note12,
                               note13=mark.note13,
                               note14=mark.note14, notes=note, coef=mark.coef_idl,
                               unite=unite_idl, text=module_idl)
    if mark.specialite == 'Reseau':
        return render_template('check_mark.html', id_student=y, name=mark.name, specialite=mark.specialite,
                               note1=mark.note1, note2=mark.note2,
                               note3=mark.note3, note4=mark.note4, note5=mark.note5, note6=mark.note6,
                               note7=mark.note7, note8=mark.note8, note9=mark.note9
                               , note10=mark.note10, note11=mark.note11, note12=mark.note12,
                               note13=mark.note13,
                               note14=mark.note14, notes=note, coef=mark.coef_rs,
                               unite=unite_rs, text=module_reseau)
    if mark.specialite == 'SE':
        return render_template('check_mark.html', id_student=y, name=mark.name, specialite=mark.specialite,
                               note1=mark.note1, note2=mark.note2,
                               note3=mark.note3, note4=mark.note4, note5=mark.note5, note6=mark.note6,
                               note7=mark.note7, note8=mark.note8, note9=mark.note9
                               , note10=mark.note10, note11=mark.note11, note12=mark.note12,
                               note13=mark.note13,
                               note14=mark.note14, notes=note, coef=mark.coef_se,
                               unite=unite_se, text=module_se)


@main.route("/all_student")
@login_required
def students():
    students = db.engine.execute("SELECT * FROM Marks")
    students = sorted(students, key=lambda k: (k["id_student"]))
    return render_template("all_student.html", students=students, name=current_user.name_teacher)
