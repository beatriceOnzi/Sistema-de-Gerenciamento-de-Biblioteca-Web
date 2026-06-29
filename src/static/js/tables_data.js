export async function get_records_table_data() {
    const response = await fetch("./get_emprestimos_record");
    const data = await response.json()
    return data
}

export async function get_cadastro_table_data() {
    const response = await fetch("./get_emprestimos_cadastro");
    const data = await response.json()
    return data
}

export async function save_title(id, title) {
    const response = await fetch(`./save_title`, {

        method: 'POST',

        headers: {
            'Content-Type': 'application/json'
        },

        body: JSON.stringify({
            id,
            title
        })
    });

    const data = await response.json()
}

export async function set_data_devolucao(title, aluno) {
    console.log("entra da funcao")
    const response = await fetch(`./set_data_devolucao`, {

        method: 'POST',

        headers: {
            'Content-Type': 'application/json'
        },

        body: JSON.stringify({
            title,
            aluno
        })
    });

    const data = await response.json()
    return data
}