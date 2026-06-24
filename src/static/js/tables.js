import { get_records_table_data } from '/static/js/tables_data.js'

const records_table_data = await get_records_table_data();

const tabledata_registro = records_table_data.map(emp => ({
    id: emp.id,
    data_empre: emp.data_emprestimo,
    aluno: emp.aluno,
    livro: emp.livro,
    data_dev_prev: emp.data_devolucao_prevista,
}));

var tabledata = [
 	{id:1, data_empre:"", aluno:"", livro:"", data_dev_prev:""},
 	];

var tabela_registro = new Tabulator("#tabela_registro", {
 	height: "100%",
    data:tabledata_registro,
 	layout:"fitColumns",
 	columns:[
	 	{title:"Data de Empréstimo", field:"data_empre", hozAlign:"center", headerWordWrap:true, headerSort: false},
	 	{title:"Aluno", field:"aluno", hozAlign:"left", formatter: "textarea", headerSort: false},
	 	{title:"Livro", field:"livro", hozAlign:"left", formatter: "textarea", headerSort: false},
	 	{title:"Data de Devolução", field:"data_dev_real", hozAlign:"center", headerWordWrap:true, headerSort: false},
 	],
});

var tabela_atual = new Tabulator("#tabela_atual", {
 	height: "100%",
 	data:tabledata,
 	layout:"fitColumns",
 	columns:[
	 	{title:"Data de Empréstimo", field:"data_empre", hozAlign:"center", headerWordWrap:true, headerSort: false},
	 	{title:"Aluno", field:"aluno",hozAlign:"left", formatter: "textarea", headerSort: false},
	 	{title:"Livro", field:"livro", hozAlign:"left", formatter: "textarea", headerSort: false},
	 	{title:"Data de Devolução", field:"data_dev_prev", hozAlign:"center", headerWordWrap:true, headerSort: false},
 	],
});
