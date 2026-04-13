async function fetchPlanes(){
    
    const response = await fetch("http://127.0.0.1:8000/flights");
    const data = await response.json();

    console.log(data);
    
}
fetchPlanes()