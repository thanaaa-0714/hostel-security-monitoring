function registerStudent(){

    const name=document.getElementById("name").value;
    const room=document.getElementById("room").value;

    fetch("/register",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            name:name,
            room:room
        })

    })

    .then(response=>response.json())

    .then(data=>{

        alert(data.message);

        loadStudents();

    });

}

function loadStudents(){

    fetch("/students")

    .then(response=>response.json())

    .then(data=>{

        let table="";

        data.forEach(student=>{

            table += `
            <tr>
                <td>${student.id}</td>
                <td>${student.name}</td>
                <td>${student.room}</td>
            </tr>
            `;

        });

        document.getElementById("studentTable").innerHTML=table;

    });

}

function scanFace(){

    fetch("/entry",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({

            name:document.getElementById("name").value

        })

    })

    .then(response=>response.json())

    .then(data=>{

        alert(data.message);

    });

}
function scanFace(){

    fetch("/scan")
    .then(response=>response.json())
    .then(data=>{
        alert(data.message);
    });

}

window.onload=function(){

    loadStudents();

}