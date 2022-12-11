// General Create Table Function
function createTable(header, data, target) {
    if (data.length == 0) {
        alertTxt = document.createElement('h1');
        alertTxt.style.color = 'Red';
        alertTxt.textContent = "No Result Found... Try something else!";
        document.getElementById(target).appendChild(alertTxt);
        return 0;
    }

    var table = document.createElement('table');
    table.classList.add("table");    // from bootstrap 
    table.classList.add("table-hover");
    table.classList.add("table-dark"); 

    // header
    var thead = document.createElement('thead');
    var row = document.createElement('tr');
    for (let i = 0; i < header.length; i++) {
        var cell = document.createElement('th');
        cell.scope = "col";
        cell.textContent = header[i];
        row.appendChild(cell);
    }
    thead.appendChild(row);
    table.appendChild(thead);

    // data
    var tbody = document.createElement('tbody');
    for (let i = 0; i < data.length; i++) {
        row = document.createElement('tr');
        for (let j = 0; j < data[i].length; j++) {
            var cell = document.createElement('td');
            if (header[j] == "F2P") {
                if (data[i][j] == "True") {
                    cell.innerHTML = "&#x274E;";
                } else {
                    cell.innerHTML = "&#x274C;";
                }
            } else if (header[j] == "Sales" || header[j] == "MarketCap") {
                cell.innerHTML = data[i][j];
            } else {
                cell.textContent = data[i][j];
            }
            row.appendChild(cell);
        }
        tbody.appendChild(row);
    }
    table.appendChild(tbody);

    // append to div
    document.getElementById(target).appendChild(table);
}

function fillDataListOptions(id, data) {
    for (let i = 0; i < data.length; i++) {
        var option = document.createElement('option');
        option.value = data[i];
        document.getElementById(id).appendChild(option);
    };
}

function fillDropDownOptions(id, data) {
    for (let i = 0; i < data.length; i++) {
        var option = document.createElement('option');
        option.value = data[i];
        option.innerHTML = data[i];
        document.getElementById(id).appendChild(option);
    };
}

function renderLoading(zone) {
    console.log('loading...');
    setInterval(function() {
        let loading = document.getElementById(zone).style.display = 'block';
    }, 1000);
}