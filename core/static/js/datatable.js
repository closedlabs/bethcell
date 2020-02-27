	$(document).ready(function() {
		$('#datatables').DataTable({
			"pagingType": "full_numbers",
			"lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]],
			responsive: true,
			searching: false, 
      "language": {
          "sProcessing":   "Processando...",
          "sLengthMenu":   " _MENU_ ",
          "sZeroRecords":  "<b><center>Não foram encontrados resultados</center><b>",
          "info": "Pág _PAGE_ de _PAGES_",
          "sInfoEmpty":    "",
          "sInfoFiltered": "",
          "sInfoPostFix":  "",
          "sSearch":       "",
          "sUrl":          "",
          "oPaginate": {
              "sFirst":    "Primeiro",
              "sPrevious": "",
              "sNext":     "",
              "sLast":     "Último"
          }
      }
    });
    var table = $('#datatables').DataTable();

        // Edit record
        table.on( 'click', '.edit', function () {
        $tr = $(this).closest('tr');

        var data = table.row($tr).data();
        alert( 'You press on Row: ' + data[0] + ' ' + data[1] + ' ' + data[2] + '\'s row.' );
        } );

        // Delete a record
        table.on( 'click', '.remove', function (e) {
        $tr = $(this).closest('tr');
        table.row($tr).remove().draw();
        e.preventDefault();
        } );

        //Like record
        table.on( 'click', '.like', function () {
        alert('You clicked on Like button');
        });

        $('.card .material-datatables label').addClass('form-group');
        });
