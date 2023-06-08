from django.shortcuts import render, redirect
from django.db import connection, connections


def index(request):
    #need database info: "SELECT column, column, column FROM table ORDER BY column"
    sqlQuery = "SELECT material.id, material.name, material.color FROM material ORDER BY material.name asc" 
    with connection.cursor() as cursor:
        cursor.execute(sqlQuery)
        rows = list(cursor.fetchall())
        cursor.close()
        connection.close()
    
    return render(request, "website/index.html", {
        "materials":rows
    })

def indexWithSort(request, sort):
    #if sort in [list_of_sortable_elements]
    if sort in ["name", "id", "formed"]:
        sqlQuery = f"SELECT material.id, material.name, material.color FROM material ORDER BY material.{sort} asc"
        with connection.cursor() as cursor:
            cursor.execute(sqlQuery)
            rows = list(cursor.fetchall())
            cursor.close()
            connection.close()
    
        return render(request, "website/index.html", {
        "materials":rows
    })

def materialInfo(request, sID):
    # need info on the database and its tables
    # f"SELECT item.info1, item.info2, item.info3 FROM item"
    #this method gives the info for each specific material
    sqlQuery = "SELECT item.info1, item.info2, item.info3, material.name FROM item "
    sqlQuery += "INNER JOIN item ON material.id = item.MaterialID WHERE material.id = " + str(sID)
    with connection.cursor() as cursor:
        cursor.execute(sqlQuery) 
        rows = list(cursor.fetchall())
        cursor.close()
        connection.close()

    return render(request, "website/item.html", {
    "info":rows})
