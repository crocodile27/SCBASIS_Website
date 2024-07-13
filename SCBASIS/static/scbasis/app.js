document.addEventListener('DOMContentLoaded', () => {
    const courseForm = document.querySelector('#courseForm');
    const competitionForm = document.querySelector('#competitionForm');
    const courseBtn = document.querySelector('#course-button');
    const competitionBtn = document.querySelector('#competition-button');
  
    // Hide both forms initially
    courseForm.style.display = "none";
    competitionForm.style.display = "none";
  
    // Function to display the correct form based on the active form value
    const showActiveForm = () => {
      const activeForm = document.querySelector('input[name="active_form"]').value;
      if (activeForm === 'competition') {
        courseForm.style.display = "block";
      } else if (activeForm === 'course') {
        competitionForm.style.display = "block";
      }
    };
  
    // Show the active form on page load
    showActiveForm();
  
    // Event listeners for buttons
    courseBtn.addEventListener('click', () => {
      competitionForm.style.display = "none";
      courseForm.style.display = "block";
      document.querySelector('input[name="active_form"]').value = 'course';
    });
  
    competitionBtn.addEventListener('click', () => {
      courseForm.style.display = "none";
      competitionForm.style.display = "block";
      document.querySelector('input[name="active_form"]').value = 'competition';
    });
  });
  