// Fetch team member contact information from bios.html
function loadContactInformation() {
    const contactList = document.getElementById('contact-list');
    
    if (!contactList) {
        console.error('Contact list element not found');
        return;
    }

    // Fetch the bios.html file
    fetch('bios.html')
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch bios.html');
            }
            return response.text();
        })
        .then(html => {
            // Create a temporary DOM element to parse the HTML
            const tempDiv = document.createElement('div');
            tempDiv.innerHTML = html;

            // Find all bio divs
            const bios = tempDiv.querySelectorAll('.bio');
            
            console.log('Found bios:', bios.length);
            
            // Create an array to store team members
            const teamMembers = [];

            bios.forEach(bio => {
                // Extract name from h3
                const nameElement = bio.querySelector('h3');
                const name = nameElement ? nameElement.textContent.trim() : '';

                // Extract position from the first p tag
                const positionElement = bio.querySelector('p');
                const position = positionElement ? positionElement.textContent.trim() : '';

                // Extract email from mailto link
                const emailLink = bio.querySelector('a[href^="mailto:"]');
                const email = emailLink ? emailLink.getAttribute('href').replace('mailto:', '') : '';

                if (name) {
                    teamMembers.push({ name, position, email });
                }
            });

            console.log('Team members:', teamMembers);

            // Sort by position hierarchy and then by name
            const positionOrder = {
                'Professor': 1,
                'Researcher': 2,
                'Postdoc': 3,
                'PhD Student': 4
            };

            teamMembers.sort((a, b) => {
                const orderA = positionOrder[a.position] || 999;
                const orderB = positionOrder[b.position] || 999;
                if (orderA !== orderB) {
                    return orderA - orderB;
                }
                return a.name.localeCompare(b.name);
            });

            // Build the contact list HTML
            let htmlContent = '';
            let currentPosition = '';

            teamMembers.forEach(member => {
                // Add position header if it's a new position
                if (member.position !== currentPosition) {
                    if (currentPosition !== '') {
                        htmlContent += '</ul></div>'; // Close previous section
                    }
                    currentPosition = member.position;
                    htmlContent += `
                        <div class="position-group" style="margin-bottom: 2em;">
                            <h3 style="color: #3498db; border-bottom: 2px solid #3498db; padding-bottom: 0.5em; margin-bottom: 1em;">${member.position}s</h3>
                            <ul style="list-style: none; padding: 0;">
                    `;
                }

                // Add member contact info
                const emailDisplay = member.email ? member.email : 'Email not available';
                const emailLink = member.email ? `<a href="mailto:${member.email}" style="color: #3498db; text-decoration: none;">${member.email}</a>` : emailDisplay;
                
                htmlContent += `
                    <li style="margin-bottom: 1.5em; padding: 1em; background: #f8f9fa; border-left: 4px solid #3498db; border-radius: 4px;">
                        <strong style="font-size: 1.1em; color: #2c3e50;">${member.name}</strong><br>
                        <span style="color: #7f8c8d; margin-top: 0.3em; display: inline-block;">
                            <i class="fas fa-envelope" style="margin-right: 0.5em;"></i>${emailLink}
                        </span>
                    </li>
                `;
            });

            if (currentPosition !== '') {
                htmlContent += '</ul></div>'; // Close last section
            }

            contactList.innerHTML = htmlContent;
        })
        .catch(error => {
            console.error('Error fetching contact information:', error);
            contactList.innerHTML = '<p style="color: red;">Error loading contact information. Please check the console for details.</p>';
        });
}

// Call the function when the page loads
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadContactInformation);
} else {
    // DOM is already loaded
    loadContactInformation();
}
