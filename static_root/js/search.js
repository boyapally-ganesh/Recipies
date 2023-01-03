const searchField = document.querySelector("#searchField");  
const recipe_data = document.querySelector("#recipe_data");
recipe_data.style.display = "none"

searchField.addEventListener("keyup", (e) =>{
    const searchValue = e.target.value;
    if (searchValue.length > 0){
        console.log("searchValue", searchValue);
        fetch("/search-recipes", {
            body: JSON.stringify({
                searchText: searchValue
            }),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {
            console.log("data", data);
            recipe_data.style.display = "block";
        });
    }
})