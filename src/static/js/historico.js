import { alternar_data_devolucao } from './tables_data.js'

const historico_data = await get_historico_data()

const table_data_historico = historico_data.map(emp => ({
    id: emp.id,
    data_emprestimo: emp.data_emprestimo,
    aluno: emp.aluno,
    livro: emp.livro,
    turma: formatar_turma(emp.turma),
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

const input_aluno = document.getElementById("alunos_pesquisa");
const input_livro = document.getElementById("livros_pesquisa");
const select_turma = document.getElementById("turma_pesquisa")
const select_pendencia = document.getElementById("filtro_pendencia");

input_aluno.addEventListener("input", debounce(aplicar_filtros));
input_livro.addEventListener("input", debounce(aplicar_filtros));
select_turma.addEventListener("change", aplicar_filtros);
select_pendencia.addEventListener("change", aplicar_filtros);

function aplicar_filtros() {
    const filtros = [];

    const aluno = input_aluno.value.trim();
    const livro = input_livro.value.trim();

    if (aluno !== "") {
        filtros.push({ field: "aluno", type: "like", value: aluno });
    }

    if (livro !== "") {
        filtros.push({ field: "livro", type: "like", value: livro });
    }

    if (select_turma.value !== "") {
        filtros.push({ field: "turma", type: "=", value: formatar_turma(select_turma.value) });
    }

    if (select_pendencia.value === "pendente") {
        filtros.push({ field: "data_devolucao", type: "=", value: null });
    } else if (select_pendencia.value === "devolvido") {
        filtros.push({ field: "data_devolucao", type: "!=", value: null });
    }

    historico.setFilter(filtros);
}

const pendente = v => v == null || v === "" || v === "null";

function formatar_turma(turma_int){ return `${turma_int}º Ano` }

function debounce(fn, delay = 250) {
    let timer;
    return (...args) => {
        clearTimeout(timer);
        timer = setTimeout(() => fn(...args), delay);
    };
}

async function get_historico_data() {
    const response = await fetch("./get_historico_data");
    const data = await response.json()
    return data
}