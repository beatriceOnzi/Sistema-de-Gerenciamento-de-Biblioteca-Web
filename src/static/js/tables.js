import { 
	get_records_table_data,
	get_cadastro_table_data,
    save_title
} from '/static/js/tables_data.js'

// Tabela Registros
const records_table_data = await get_records_table_data();

const tabledata_registro = records_table_data.map(emp => ({
    id: emp.id,
    data_empre: emp.data_emprestimo,
    aluno: emp.aluno,
    livro: emp.livro,
    data_dev_real: emp.data_devolucao
}));

var tabela_registro = new Tabulator("#tabela_registro", {
    height: "100%",
    data: tabledata_registro,
    layout: "fitColumns",
    columns: [
        { title: "Data de Empréstimo", field: "data_empre",     hozAlign: "center", headerWordWrap: true, headerSort: false },
        { title: "Aluno",              field: "aluno",          hozAlign: "left",   formatter: "textarea", headerSort: false },
        { title: "Livro",              field: "livro",          hozAlign: "left",   formatter: "textarea", headerSort: false },
        { title: "Data de Devolução",  field: "data_dev_real",  hozAlign: "center", headerWordWrap: true,  headerSort: false, formatter: devolucao_pendente_style },
    ],
});

// Tabela Atual
const cadastro_table_data = await get_cadastro_table_data();

const tabledata_cadastro = cadastro_table_data.map(emp => ({
    id: emp.id,
    data_empre: emp.data_emprestimo,
    aluno: emp.aluno,
    livro: emp.livro,
    data_dev_prev: emp.data_devolucao_prevista
}));

var tabela_atual = new Tabulator("#tabela_atual", {
 	height: "100%",
 	data:tabledata_cadastro,
 	layout:"fitColumns",
 	columns:[
	 	{title:"Data de Empréstimo", field:"data_empre", hozAlign:"center", headerWordWrap:true, headerSort: false},
	 	{title:"Aluno", field:"aluno",hozAlign:"left", formatter: "textarea", headerSort: false},
	 	{title:"Livro", field:"livro", hozAlign:"left", formatter: "textarea", editor:"input", headerSort: false, cellEdited: handle_save_title },
	 	{title:"Data de Devolução", field:"data_dev_prev", hozAlign:"center", headerWordWrap:true, headerSort: false},
	],
});

function handle_save_title(cell){
    var title = cell.getValue();
    var id = cell.getRow().getData().id;
    save_title(id, title)
}

function devolucao_pendente_style(cell, formatterParams, onRendered) {
    var value = cell.getValue();

    if (value == null || value == "" || value == "null") {
            cell.getElement().style.cssText += "background-color: #EB2D2DBF;";
    }
    return value ?? "Pendente";
}