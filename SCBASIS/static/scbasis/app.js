document.addEventListener('DOMContentLoaded', () => {
    const courseForm = document.querySelector('#courseForm');
    const competitionForm = document.querySelector('#competitionForm');
    const courseBtn = document.querySelector('#course-button');
    const competitionBtn = document.querySelector('#competition-button');
    
    // Initial state
    competitionForm.style.display = "none";
    courseForm.style.display = "none";
    
    // Show course form, hide competition form
    courseBtn.addEventListener('click', () => {
        competitionForm.style.display = "none";
        courseForm.style.display = "block";
    });
    
    // Show competition form, hide course form
    competitionBtn.addEventListener('click', () => {
        courseForm.style.display = "none";
        competitionForm.style.display = "block";
    });
});
