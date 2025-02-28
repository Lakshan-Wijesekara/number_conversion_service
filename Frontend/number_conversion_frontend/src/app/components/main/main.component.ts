import { Component } from '@angular/core';
import { SoapService } from '../../services/soap.service';

@Component({
  selector: 'app-main',
  standalone: false,
  templateUrl: './main.component.html',
  styleUrl: './main.component.css'
})
export class MainComponent {
  fieldValue: number = 0
  wordsResult: string = '';

  constructor(private soapService: SoapService){}

  getNumberToWords() {
    this.soapService.numberToWords(this.fieldValue).subscribe({
      next: (result) => this.wordsResult = result.words,
      error: (err) => this.wordsResult = `Error: ${err.error.error}`
    });
  }
}
