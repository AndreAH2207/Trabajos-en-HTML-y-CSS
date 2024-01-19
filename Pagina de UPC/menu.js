const portafolio = document.querySelector("#portafolio");
const services = document.querySelector("#services");

portafolio.addEventListener ("click", (p) => {
    p.preventDefault();

    const sectionP= document.querySelector(".portafolio");
    sectionP.scrollIntoView({behavior: "smoth"});

})

services.addEventListener("click", (s) =>{
    s.preventDefault();

    const sectionS= document.querySelector(".services");
    sectionS.scrollIntoView({behavior: "smoth"});

})