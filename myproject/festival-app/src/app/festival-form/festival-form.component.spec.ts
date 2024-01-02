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
    try {
      // Voer hier de logica uit om het formulier in te dienen (HTTP-verzoek)
      // Update het responseMessage op basis van het resultaat
      this.responseMessage = 'Festival created successfully!';
    } catch (error) {
      console.error('Error:', error);
      this.responseMessage = 'Error creating festival.';
    }
  }
}

