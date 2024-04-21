"""
--------------------------------------------
Get:
    query Query {
        allFilms {
            films {
                title
            }
        }
    }
--------------------------------------------
Upadate:
    mutation {
        updateFruit(
            id: 1
            scientific_name: "mangiferaa"
            tree_name: "mangifera indicaa"
            fruit_name: "Mangooo"
            family: "Anacardiaceae"
            origin: "Indiana"
            description: "Mango is green"
            bloom: "Summer"
            maturation_fruit: "Mango"
            life_cycle: "101"
            climatic_zone: "humid"
        ) {
            id
            scientific_name
            tree_name
            fruit_name
            description
        }
    }
--------------------------------------------
Post:
    mutation {
        addFruit(
            id: 1
            scientific_name: "mangifera"
            tree_name: "mangifera indica"
            fruit_name: "Mango"
            family: "Anacardiaceae"
            origin: "India"
            description: "Mango is yellow"
            bloom: "Summer"
            maturation_fruit: "Mango"
            life_cycle: "100"
            climatic_zone: "humid"
        ) {
            id
            scientific_name
            tree_name
            fruit_name
            origin
        }
    }
--------------------------------------------
Delete:
    mutation{
        deleteFruit(id: 3){
            fruit_name
            scientific_name
            tree_name
        }
    }
--------------------------------------------


Для запроса данны используется 
    query{
     
    }

    Для запроса делаем 
        query А{
            s1{}
        }
        query B{
            s2{}
        }
    or
        query AandB{
            somecount(statu:open){
                s1{}
                s1{}
            }
        }

"""