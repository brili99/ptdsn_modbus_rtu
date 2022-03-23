<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <script src="jquery-3.6.0.min.js"></script>

    <style>
        table,
        th,
        td {
            border: 1px solid;
        }
    </style>
</head>

<body style='display:flex; flex-direction:column; justify-content:center; min-height:100vh; align-items: center; text-align: center;'>
    <table>
        <tr>
            <th>Variabel</th>
            <th>Nilai</th>
        </tr>
        <tr>
            <td>Data 1</td>
            <td id="d1"></td>
        </tr>
        <tr>
            <td>Data 2</td>
            <td id="d2"></td>
        </tr>
        <tr>
            <td>Data 3</td>
            <td id="d3"></td>
        </tr>
        <tr>
            <td>Data 4</td>
            <td id="d4"></td>
        </tr>
        <tr>
            <td>Data 5</td>
            <td id="d5"></td>
        </tr>
        <tr>
            <td>Data 6</td>
            <td id="d6"></td>
        </tr>
        <tr>
            <td>Data 7</td>
            <td id="d7"></td>
        </tr>
        <tr>
            <td>Data 8</td>
            <td id="d8"></td>
        </tr>
    </table>
    <script>
        setInterval(function() {
            $.getJSON("status.php", function(data) {
                $.each(data, function(key, val) {
                    // if (val['nama'] == "1") $('#d1').html(val['nilai']);
                    // if (val['nama'] == "2") $('#d2').html(val['nilai']);
                    // if (val['nama'] == "3") $('#d3').html(val['nilai']);
                    // if (val['nama'] == "4") $('#d4').html(val['nilai']);
                    // if (val['nama'] == "5") $('#d5').html(val['nilai']);
                    // if (val['nama'] == "6") $('#d6').html(val['nilai']);
                    // if (val['nama'] == "7") $('#d7').html(val['nilai']);
                    // if (val['nama'] == "8") $('#d8').html(val['nilai']);
                    $('#d' + val['nama']).html(val['nilai']);
                });
            });
        }, 1000);
    </script>
</body>

</html>