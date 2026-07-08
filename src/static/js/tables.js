import { 
	get_records_table_data,
	get_cadastro_table_data,
    save_title,
    set_data_devolucao,
    get_livros
} from './tables_data.js'


// Tabela Registros
const records_table_data = await get_records_table_data();

const tabledata_registro = records_table_data.map(emp => ({
    id: emp.id,
    aluno_id: emp.aluno_id,
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
    aluno_id: emp.aluno_id,
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
	 	{title:"Livro", field:"livro", hozAlign:"left", formatter: "textarea", editor:"input", headerSort: false,
            editor:"list",
            editorParams:{
                values:get_livros(),
                autocomplete:true,
                filterRemote:false,
                freetext:true,
                allowEmpty:true,
                listOnEmpty:false,
                placeholderEmpty: "",
                filterFunc: function(term, label, value, item){
                    return label.toLowerCase().startsWith(term.toLowerCase());
                }
            },
            cellEdited: salvar_emprestimo
        },
	 	{title:"Data de Devolução", field:"data_dev_prev", hozAlign:"center", headerWordWrap:true, headerSort: false},
	],
});

async function salvar_emprestimo(cell){
    let title = cell.getValue();
    title = title.trim()
    const id = cell.getRow().getData().id;
    const aluno_id = cell.getRow().getData().aluno_id;
    const aluno = cell.getRow().getData().aluno;

    await save_title(id, title);
    const data_devolucao = await set_data_devolucao(title, aluno);
    console.log(data_devolucao);

    const row = tabela_registro.getRows().find(
        row => row.getData().aluno_id === aluno_id
    );

    if (row) {
        row.update({
            data_dev_real: data_devolucao
        });
    }
    row.reformat();
}

function devolucao_pendente_style(cell) {
    let value = cell.getValue();
    let livro = cell.getRow().getData().livro;
    let pendente;

    if (!value && livro) {
        cell.getElement().style.cssText += "background-color: #EB2D2DBF; color: #222";
        pendente = "Pendente";
    }

    return !livro ? pendente : value
}