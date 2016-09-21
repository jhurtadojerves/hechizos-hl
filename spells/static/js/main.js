var libro = document.getElementById('libro')
var libros = document.getElementById('libros')

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
