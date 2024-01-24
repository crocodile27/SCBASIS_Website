document.addEventListener('DOMContentLoaded',()=>{
	const courseForm = document.querySelector('#courseForm')
	const competitionForm = document.querySelector('#competitionForm')
	const courseBtn = document.querySelector('#course-button')
	const competitionBtn = document.querySelector('#competition-button')
	console.log('success')
	competitionForm.style.display = "None"
	courseForm.style.display = "None"
	courseBtn.addEventListener('click',() => {
		competitionForm.style.display = "None"
		courseForm.style.display = "Block"

		console.log("1")

	})
	competitionBtn.addEventListener('click',() => {
		courseForm.style.display = "None"
		competitionForm.style.display = "Block"
		
		console.log("2")

	})







})
