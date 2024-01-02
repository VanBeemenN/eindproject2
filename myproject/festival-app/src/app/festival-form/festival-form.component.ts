import { Component } from '@angular/core';

@Component({
  selector: 'app-festival-form',
  templateUrl: './festival-form.component.html',
  styleUrls: ['./festival-form.component.css']
})
export class FestivalFormComponent {
  formData = {
    naam: '',
    locatie: '',
    start_datum: '',
    eind_datum: ''
  };

  responseMessage = '';

  submitForm(): void {
    const formData = {
      naam: this.formData.naam,
      locatie: this.formData.locatie,
      start_datum: this.formData.start_datum,
      eind_datum: this.formData.eind_datum
    };

    fetch('http://127.0.0.1:8000/create_festival', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    })
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
      this.responseMessage = 'Festival created successfully!';
    })
    .catch((error) => {
      console.error('Error:', error);
      this.responseMessage = 'Error creating festival.';
    });
  }

  getFestivals(): void {
    fetch('http://127.0.0.1:8000/festivals')
      .then(response => response.json())
      .then(data => {
        console.log('Festivals Data:', data);
        // Verwerk de festivalsData zoals gewenst
      })
      .catch(error => console.error('Error:', error));
  }

  getLanden(): void {
    fetch('http://127.0.0.1:8000/landen')
      .then(response => response.json())
      .then(data => {
        console.log('Landen Data:', data);
        // Verwerk de landenData zoals gewenst
      })
      .catch(error => console.error('Error:', error));
  }

  getCurrentUser(): void {
    fetch('http://127.0.0.1:8000/users/me', {
      headers: {
        'Authorization': 'Basic ' + btoa('your-username:your-password') // Vervang met de echte referenties
      }
    })
      .then(response => response.json())
      .then(data => {
        console.log('User Data:', data);
        // Verwerk de userData zoals gewenst
      })
      .catch(error => console.error('Error:', error));
  }
}
