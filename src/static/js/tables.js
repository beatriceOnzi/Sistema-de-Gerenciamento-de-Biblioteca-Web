var tabledata = [
 	{id:1, data_empre:"17-06-2026", aluno:"Oli Bob", livro:"O principe encantado e a princesa amaldiçoada", data_dev_prev:"24-06-2026"},
 	{id:2, data_empre:"17-06-2026", aluno:"Mary May", livro:"blue", data_dev_prev:"24-06-2026"},
 	{id:3, data_empre:"17-06-2026", aluno:"Christine Lobowski", livro:"green", data_dev_prev:"24-06-2026"},
 	{id:4, data_empre:"17-06-2026", aluno:"Brendon Philips", livro:"orange", data_dev_prev:"24-06-2026"},
 	{id:5, data_empre:"17-06-2026", aluno:"Margret Marmajuke", livro:"yellow", data_dev_prev:"24-06-2026"},
 ];

 
var tabela_registro = new Tabulator("#tabela_registro", {
 	height: "100%",
    data:tabledata,
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
