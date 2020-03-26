const search = document.getElementById('busqueda')

search.addEventListener('keyup', async () => {
  const output = document.getElementById('resultados')
  
  let param = search.value
  
  const response = await fetch(`/api/spells/?search=${param}`)
  const data = await response.json()
  const {results} = data
  output.innerHTML = ''
  
  results.map((spell, index) => {
    const line = document.createElement('a')
    line.href = `/spells/${spell.slug}`
    line.text = spell.name
    line.classList.add('Search-resultados--item')
    if (index % 2 !== 0) {
      line.classList.add('Search-resultados--info')
    }
    resultados.appendChild(line)
    if (param === '')
      output.innerHTML = ''
  })
})