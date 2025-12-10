// Fetch the JSON file and populate the publications section
fetch("./publications.json")
    .then(response => response.json())
    .then(publications => {
        let publicationsHTML = "";

        publications.forEach((pub, index) => {
            const abstractId = `abstract-${index}`;
            const hasAbstract = pub.abstract && pub.abstract !== "No abstract available";
            
            publicationsHTML += `
                <table class="publication-table" border="1" style="width:100%; margin-bottom: 20px; border-collapse: collapse;">
                    <tr>
                        <td style="width: 20%; font-weight: bold;">${pub.date}</td>
                        <td style="width: 80%;">
                            <a href="${pub.link}" target="_blank">${pub.title}</a>
                        </td>
                    </tr>
                    <tr>
                        <td></td>
                        <td>
                            <em>${pub.authors}</em>
                            ${hasAbstract ? `
                            <br>
                            <button onclick="toggleAbstract('${abstractId}')" 
                                    style="margin-top: 8px; padding: 4px 12px; font-size: 0.85em; 
                                           background-color: #f0f0f0; border: 1px solid #ccc; 
                                           border-radius: 4px; cursor: pointer;">
                                Read abstract
                            </button>
                            <div id="${abstractId}" style="display: none; margin-top: 10px; 
                                 padding: 10px; background-color: #f9f9f9; border-left: 3px solid #333; 
                                 font-style: normal; line-height: 1.6;">
                                ${pub.abstract}
                            </div>
                            ` : ''}
                        </td>
                    </tr>
                </table>
            `;
        });

        // Insert the formatted publications into the div
        document.getElementById("publications-list").innerHTML = publicationsHTML;
    })
    .catch(error => console.error("Error loading publications:", error));

// Function to toggle abstract visibility
function toggleAbstract(abstractId) {
    const abstractDiv = document.getElementById(abstractId);
    const button = event.target;
    
    if (abstractDiv.style.display === "none") {
        abstractDiv.style.display = "block";
        button.textContent = "Hide abstract";
    } else {
        abstractDiv.style.display = "none";
        button.textContent = "Read abstract";
    }
}