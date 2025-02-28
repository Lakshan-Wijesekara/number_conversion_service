import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SoapService {

  private apiURL = 'http://127.0.0.1:5000'
  constructor(private http: HttpClient) { }

  numberToWords(number: number): Observable<any> {
    return this.http.get(`${this.apiURL}/api/number-to-words`, { params: { number: number.toString() } } )
  }
}
