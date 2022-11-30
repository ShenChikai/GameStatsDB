data = [
    {
        name: "name1",
        age: 11,
        gender: "male"
    },
    {
        name: "name2",
        age: 27,
        gender: "male"
    },
    {
        name: "name3",
        age: 36,
        gender: "female"
    },
    {
        name: "name4",
        age: 42,
        gender: "male"
    },
    {
        name: "name5",
        age: 55,
        gender: "female"
    },
]


var table = document.createElement('table');
table.classList.add("table");    // from bootstrap 
table.classList.add("table-hover");
table.classList.add("table-dark"); 

// header
var thead = document.createElement('thead');
var row = document.createElement('tr');
var cell = document.createElement('th');    // Index Header
cell.scope = "col";
cell.textContent = "Index";
row.appendChild(cell);
for (const prop in data[0]) {
    var cell = document.createElement('th');
    cell.scope = "col";
    cell.textContent = prop;
    row.appendChild(cell);
}
thead.appendChild(row);
table.appendChild(thead);

// data
var tbody = document.createElement('tbody');
for (var i = 0; i < data.length; i++) {
    row = document.createElement('tr');
    var cell = document.createElement('th');    // Row Num
    cell.scope = "row";
    cell.textContent = i;
    row.appendChild(cell);
    for (const prop in data[0]) {
        var cell = document.createElement('td');
        cell.textContent = data[i][prop];
        row.appendChild(cell);
    }
    tbody.appendChild(row);
}
table.appendChild(tbody);

// append to div
document.getElementById('tableDiv').appendChild(table);