(function () {

    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('Está seguro de eliminar la receta?');
            if (!confirmacion) {
                e.preventDefault();
            }
        })
    })
})


function confirmarEliminacion(codigo) {
    if (confirm("¿Estás seguro de que deseas eliminar esta receta?")) {
      // Si el usuario confirma, redirige a la URL de eliminación
      window.location.href = "/eliminarReceta/" + codigo;
    }
  }

  setTimeout(function() {
    var autoFadeAlert = document.getElementById('auto-fade-alert');
    autoFadeAlert.style.opacity = '0';
    setTimeout(function() {
      autoFadeAlert.style.display = 'none';
    }, 2000); 
  }, 3000);




