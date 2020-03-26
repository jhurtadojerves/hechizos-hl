let libro = document.getElementById('libro')
let libros = document.getElementById('libros')

libro.addEventListener('click', function(e){
    e.preventDefault()
    if (libros.style.display == 'none')
    {
        libros.style.display = 'block'
    }
    else
    {
        libros.style.display = 'none'
    }
})
