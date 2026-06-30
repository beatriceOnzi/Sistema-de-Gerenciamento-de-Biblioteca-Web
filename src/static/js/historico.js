console.log("funciona")
const data = [
    {
        data_empre: "03-02-2026",
        aluno: "Ana Souza",
        livro: "Dom Casmurro",
        turma: "8º Ano",
        data_dev_real: "10-02-2026"
    },
    {
        data_empre: "05-02-2026",
        aluno: "Carlos Oliveira",
        livro: "O Pequeno Príncipe",
        turma: "7º Ano",
        data_dev_real: "Pendente"
    },
    {
        data_empre: "06-02-2026",
        aluno: "Mariana Lima",
        livro: "Harry Potter e a Pedra Filosofal",
        turma: "6º Ano",
        data_dev_real: "13-02-2026"
    },
    {
        data_empre: "08-02-2026",
        aluno: "João Pedro",
        livro: "Capitães da Areia",
        turma: "9º Ano",
        data_dev_real: "Pendente"
    },
    {
        data_empre: "09-02-2026",
        aluno: "Beatriz Fernandes",
        livro: "A Bolsa Amarela",
        turma: "5º Ano",
        data_dev_real: "16-02-2026"
    },
    {
        data_empre: "10-02-2026",
        aluno: "Lucas Martins",
        livro: "Percy Jackson e o Ladrão de Raios",
        turma: "8º Ano",
        data_dev_real: "17-02-2026"
    },
    {
        data_empre: "11-02-2026",
        aluno: "Fernanda Rocha",
        livro: "O Menino Maluquinho",
        turma: "4º Ano",
        data_dev_real: "Pendente"
    },
    {
        data_empre: "12-02-2026",
        aluno: "Gabriel Costa",
        livro: "Diário de um Banana",
        turma: "6º Ano",
        data_dev_real: "19-02-2026"
    }
];

var tabela_registro = new Tabulator("#tabela_historico", {
    height: "100%",
    data: data,
    layout: "fitColumns",
    columns: [
        { title: "Data de Empréstimo", field: "data_empre", hozAlign: "center", headerWordWrap: true, headerSort: false },
        { title: "Aluno", field: "aluno", hozAlign: "left", formatter: "textarea", headerSort: false },
        { title: "Livro", field: "livro", hozAlign: "left", formatter: "textarea", headerSort: false },
        { title: "Turma", field: "turma", hozAlign: "left", headerSort: false },
        { title: "Data de Devolução", field: "data_dev_real", hozAlign: "center", headerWordWrap: true, headerSort: false, formatter: devolucao_pendente_style },
    ],
});

function devolucao_pendente_style(cell) {
    var value = cell.getValue();

    if (value == null || value == "" || value == "null") {
            cell.getElement().style.cssText += "background-color: #EB2D2DBF; color: #222";
    }
    return value ?? "Pendente";
}