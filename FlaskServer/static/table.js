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

// header
var row = document.createElement('tr');
for (const prop in data[0]) {
    var cell = document.createElement('th');
    cell.textContent = prop;
    row.appendChild(cell);
}
table.appendChild(row);

// data
for (var i = 0; i < data.length; i++) {
    row = document.createElement('tr');
    for (const prop in data[0]) {
        var cell = document.createElement('td');
        cell.textContent = data[i][prop];
        row.appendChild(cell);
    }
    table.appendChild(row);
}

// append to div
document.getElementById('tableDiv').appendChild(table);