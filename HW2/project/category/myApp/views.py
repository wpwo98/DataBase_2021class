from django.shortcuts import render
from django.db import connection
import pandas as pd
import os
import django
import csv
import sys

CSV_STUD='./templates/myApp/folder/students.csv'
CSV_PROF='./templates/myApp/folder/professors.csv'
CSV_COUNTY='./templates/myApp/folder/counties.csv'
CSV_COVID='./templates/myApp/folder/COVID.csv'
'''
data = None
file_dir = './templates/myApp/folder'
def read():
    with open('CSV_STUD', 'r') as file:
        data_reader = csv.DictReader(file)
        s = pd.DataFrame(data_reader)
    ss=[]
    for row in range(len(s)):
        st=(s['studentId'][row], s['name'][row], s['score'][row], s['county'][row])
        ss.apend(st)
    for i in range(len(s)):
        Students.objects.create(studentId=ss[i][0],name=ss[i][1],score=ss[i][2],county=ss[i][3])
'''
def display_stud(request):
    outputStudents = []
    with connection.cursor() as cursor:
        empdata = pd.read_csv('./myApp/templates/myApp/folder/students.csv', header=None, delimiter = ',')
        empdata.head()
        cursor.execute('DROP TABLE IF EXISTS students;')
        cursor.execute("CREATE TABLE students(studentID char(30),name char(30),score real,county char(30))")

        for i,row in empdata.iterrows():
            #here %S means string values
            sql = "INSERT INTO categorydb.students VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            # the connection is not auto committed by default, so we must commit to save our changes
            connection.commit()

        sqlQueryStudents = "SELECT Students.studentID, Name, score, county FROM categorydb.Students;"
        cursor.execute(sqlQueryStudents)
        fetchResultStudents = cursor.fetchall()
        connection.commit()
        connection.close()

        for temp in fetchResultStudents:
            eachRow = {'studentID': temp[0], 'name': temp[1], 'score': temp[2], 'county': temp[3]}
            outputStudents.append(eachRow)
    return render(request, 'myApp/index.html',{"Students": outputStudents})


def display_prof(request):
    outputProfessors = []
    with connection.cursor() as cursor:
        empdata = pd.read_csv('./myApp/templates/myApp/folder/professors.csv', header=None, delimiter = ',')
        empdata.head()
        cursor.execute('DROP TABLE IF EXISTS professors;')
        cursor.execute("CREATE TABLE professors(facultyID char(30),name char(30),age int,county char(30))")
        for i,row in empdata.iterrows():
            #here %S means string values
            sql = "INSERT INTO categorydb.professors VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            # the connection is not auto committed by default, so we must commit to save our changes
            connection.commit()

        sqlQueryProfessors = "SELECT Professors.facultyID, name, age, county FROM categorydb.Professors;"
        cursor.execute(sqlQueryProfessors)
        fetchResultProfessors = cursor.fetchall()
        connection.commit()
        connection.close()

        for temp in fetchResultProfessors:
            eachRow = {'facultyid': temp[0], 'professorname': temp[1], 'age': temp[2], 'county': temp[3]}
            outputProfessors.append(eachRow)

    return render(request, 'myApp/index.html',{"Professors": outputProfessors})


def display_county(request):
    outputCounties = []
    with connection.cursor() as cursor:
        empdata = pd.read_csv('./myApp/templates/myApp/folder/counties.csv', header=None, delimiter = ',')
        empdata.head()
        cursor.execute('DROP TABLE IF EXISTS counties;')
        cursor.execute("CREATE TABLE counties(countyName char(30),population int,city char(30))")
        for i,row in empdata.iterrows():
            #here %S means string values
            sql = "INSERT INTO categorydb.counties VALUES (%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            # the connection is not auto committed by default, so we must commit to save our changes
            connection.commit()
        sqlQueryCounties = "SELECT Counties.countyName, population, city FROM categorydb.Counties;"
        cursor.execute(sqlQueryCounties)
        fetchResultCounties = cursor.fetchall()

        connection.commit()
        connection.close()

        for temp in fetchResultCounties:
            eachRow = {'countyname': temp[0], 'population': temp[1], 'city': temp[2]}
            outputCounties.append(eachRow)

    return render(request, 'myApp/index.html',{"Counties": outputCounties})


def display_covid(request):
    outputCOVID = []
    with connection.cursor() as cursor:
        empdata = pd.read_csv('./myApp/templates/myApp/folder/covid.csv', header=None, delimiter = ',')
        empdata.head()
        cursor.execute('DROP TABLE IF EXISTS covid;')
        cursor.execute("CREATE TABLE covid(patientID char(30), city char(30))")
        for i,row in empdata.iterrows():
            #here %S means string values
            sql = "INSERT INTO categorydb.covid VALUES (%s,%s)"
            cursor.execute(sql, tuple(row))
            # the connection is not auto committed by default, so we must commit to save our changes
            connection.commit()
        sqlQueryCOVID = "SELECT COVID.patientid, city FROM categorydb.COVID;"
        cursor.execute(sqlQueryCOVID)
        fetchResultCOVID = cursor.fetchall()

        connection.commit()
        connection.close()

        for temp in fetchResultCOVID:
            eachRow = {'patientid': temp[0], 'city': temp[1]}
            outputCOVID.append(eachRow)

    return render(request, 'myApp/index.html',{"COVID": outputCOVID})


def display(request):
    outputStudents = []
    outputProfessors = []
    outputCounties = []
    outputCOVID = []
    outputQuery1 = []
    outputQuery2 = []
    outputQuery3 = []
    outputQuery4 = []
    outputQuery5 = []

    with connection.cursor() as cursor:
        empdata = pd.read_csv('./myApp/templates/myApp/folder/students.csv', header=None, delimiter = ',')
        empdata.head()
        cursor.execute('DROP TABLE IF EXISTS students;')
        cursor.execute("CREATE TABLE students(studentID char(30),name char(30),score real,county char(30))")
        for i,row in empdata.iterrows():
            #here %S means string values
            sql = "INSERT INTO categorydb.students VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            # the connection is not auto committed by default, so we must commit to save our changes
            connection.commit()
        sqlQueryStudents = "SELECT studentID, students.name, score, county FROM categorydb.Students;"
        cursor.execute(sqlQueryStudents)
        fetchResultStudents = cursor.fetchall()


        empdata = pd.read_csv('./myApp/templates/myApp/folder/professors.csv', header=None, delimiter = ',')
        empdata.head()
        cursor.execute('DROP TABLE IF EXISTS professors;')
        cursor.execute("CREATE TABLE professors(facultyID char(30),name char(30),age int,county char(30))")
        for i,row in empdata.iterrows():
            #here %S means string values
            sql = "INSERT INTO categorydb.professors VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            # the connection is not auto committed by default, so we must commit to save our changes
            connection.commit()
        sqlQueryProfessors = "SELECT Professors.facultyID, name, age, county FROM categorydb.Professors;"
        cursor.execute(sqlQueryProfessors)
        fetchResultProfessors = cursor.fetchall()


        empdata = pd.read_csv('./myApp/templates/myApp/folder/counties.csv', header=None, delimiter = ',')
        empdata.head()
        cursor.execute('DROP TABLE IF EXISTS counties;')
        cursor.execute("CREATE TABLE counties(countyName char(30),population int,city char(30))")
        for i,row in empdata.iterrows():
            #here %S means string values
            sql = "INSERT INTO categorydb.counties VALUES (%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            # the connection is not auto committed by default, so we must commit to save our changes
            connection.commit()
        sqlQueryCounties = "SELECT Counties.countyName, population, city FROM categorydb.Counties;"
        cursor.execute(sqlQueryCounties)
        fetchResultCounties = cursor.fetchall()


        empdata = pd.read_csv('./myApp/templates/myApp/folder/covid.csv', header=None, delimiter = ',')
        empdata.head()
        cursor.execute('DROP TABLE IF EXISTS covid;')
        cursor.execute("CREATE TABLE covid(patientID char(30), city char(30))")
        for i,row in empdata.iterrows():
            #here %S means string values
            sql = "INSERT INTO categorydb.covid VALUES (%s,%s)"
            cursor.execute(sql, tuple(row))
            # the connection is not auto committed by default, so we must commit to save our changes
            connection.commit()
        sqlQueryCOVID = "SELECT COVID.patientid, city FROM categorydb.COVID;"
        cursor.execute(sqlQueryCOVID)
        fetchResultCOVID = cursor.fetchall()


        sqlQueryQuery1 = "SELECT county, ROUND(AVG(score),4) FROM categorydb.Students GROUP BY county ORDER BY county ASC;"
        cursor.execute(sqlQueryQuery1)
        fetchResultQuery1 = cursor.fetchall()

        sqlQueryQuery2 = "SELECT city, round(AVG(score),4) FROM categorydb.Students, categorydb.Counties " \
                         "WHERE Students.county=Counties.countyName GROUP BY city ORDER BY city ASC;"
        cursor.execute(sqlQueryQuery2)
        fetchResultQuery2 = cursor.fetchall()

        sqlQueryQuery5 = "SELECT students.name, city1 " \
                         "FROM( SELECT count/sum AS ratio, count, sum, city1, city2 " \
                         "  FROM ( SELECT covid.city AS city1, count(covid.city) AS count FROM categorydb.covid GROUP BY covid.city)a, " \
                         "  (SELECT counties.city AS city2, SUM(counties.population) AS sum FROM categorydb.counties GROUP BY counties.city)b " \
                         "  WHERE city1=city2 ORDER BY 1/ratio LIMIT 3)c, categorydb.students, categorydb.counties " \
                         "WHERE city1=counties.city AND counties.countyName=students.county ORDER BY 1/ratio;"
        cursor.execute(sqlQueryQuery5)
        fetchResultQuery5 = cursor.fetchall()

        connection.commit()
        connection.close()

        for temp in fetchResultStudents:
            eachRow = {'studentid': temp[0], 'studentname': temp[1], 'score': temp[2], 'county': temp[3]}
            outputStudents.append(eachRow)

        for temp in fetchResultProfessors:
            eachRow = {'facultyid': temp[0], 'professorname': temp[1], 'age': temp[2], 'county': temp[3]}
            outputProfessors.append(eachRow)

        for temp in fetchResultCounties:
            eachRow = {'countyname': temp[0], 'population': temp[1], 'city': temp[2]}
            outputCounties.append(eachRow)

        for temp in fetchResultCOVID:
            eachRow = {'patientid': temp[0], 'city': temp[1]}
            outputCOVID.append(eachRow)

        for temp in fetchResultQuery1:
            eachRow = {'county': temp[0], 'avgScore': temp[1]}
            outputQuery1.append(eachRow)

        for temp in fetchResultQuery2:
            eachRow = {'cityName': temp[0], 'avgScore': temp[1]}
            outputQuery2.append(eachRow)

        for temp in fetchResultQuery5:
            eachRow = {'name': temp[0], 'city1': temp[1]}
            outputQuery5.append(eachRow)

    return render(request, 'myApp/index.html',{"Students": outputStudents, "Professors": outputProfessors,
                                               "Counties": outputCounties, "COVID": outputCOVID,
                                               "Query1": outputQuery1, "Query2": outputQuery2,
                                               "Query5": outputQuery5},)

