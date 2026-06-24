export async function get_records_table_data() {
    const response = await fetch("./get_emprestimos_record");
    const data = await response.json()
    return data
}
