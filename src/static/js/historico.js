const historico_data = await get_historico_data()

const table_data_historico = historico_data.map(emp => ({
    id: emp.id,
    data_emprestimo: emp.data_emprestimo,
    aluno: emp.aluno,
    livro: emp.livro,
    turma: emp.turma,
    data_devolucao: emp.data_devolucao
}));

var historico = new Tabulator("#tabela_historico", {
    height: "100%",
    data: table_data_historico,
    layout: "fitColumns",
    columns: [
        { title: "Data de Empréstimo", field: "data_emprestimo", hozAlign: "center", headerWordWrap: true, headerSort: false },
        { title: "Aluno", field: "aluno", hozAlign: "left", formatter: "textarea", headerSort: false },
        { title: "Livro", field: "livro", hozAlign: "left", formatter: "textarea", headerSort: false },
        { title: "Turma", field: "turma", hozAlign: "center", headerSort: false },
        { 
            title: "Data de Devolução", 
            field: "data_devolucao", 
            hozAlign: "center", 
            headerWordWrap: true, 
            headerSort: false, 
            formatter: devolucao_pendente_style,
            cellClick: alternar_data_devolucao,
        },
    ],
});

function devolucao_pendente_style(cell) {
    var value = cell.getValue();

    if (value == null || value == "" || value == "null") {
            cell.getElement().style.cssText += "background-color: #EB2D2DBF; color: #222";
    }
    return value ?? "Pendente";
}

async function get_historico_data() {
    const response = await fetch("./get_historico_data");
    const data = await response.json()
    return data
}

async function alternar_data_devolucao(e, cell) {
    const id = cell.getRow().getData().id;
    const conteudo_data_devolucao = await atualizar_data_devolucao(id);

    const row = cell.getRow()

    if (row) {
        row.update({
            data_devolucao: conteudo_data_devolucao
        });
    }

    row.reformat();
}

async function atualizar_data_devolucao(id){
    const response = await fetch(`./atualizar_data_devolucao`, {
        method: 'POST',

        headers: {
            'Content-Type': 'application/json'
        },

        body: JSON.stringify({
            id
        })
    });

    const data = await response.json()

    return data
}