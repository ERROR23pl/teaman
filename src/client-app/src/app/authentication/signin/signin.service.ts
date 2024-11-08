import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders, HttpParams} from '@angular/common/http';
import {environment} from '../../../environments/environment';
import {catchError, Observable} from 'rxjs';
import {AccessToken, TokenRequest, TokenResponse} from '../../data.interfaces';
@Injectable({
  providedIn: 'root'
})
export class SigninService {
  private apiURL: string = `${environment.apiURL}/token`
  private accessToken?: AccessToken
  private httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/x-www-form-urlencoded',
      'accept': 'application/json'
    }),
    withCredentials: true
  };


  constructor(private http: HttpClient) { }

  private handleError(error: any, caught: Observable<Object>): Observable<Object> {
    console.error('Error occurred:', error);
    throw caught;
  }

  fetchAuthToken(credentials: TokenRequest): Observable<TokenResponse> {
    let errorMsg: string = ""
    console.log("request body: ", credentials)

    const body = new HttpParams()
      .set('grant_type', credentials.grant_type)
      .set('username', credentials.username)
      .set('password', credentials.password)
      .set('scope', credentials.scope || '')
      .set('client_id', credentials.client_id)
      .set('client_secret', credentials.client_secret)

    const result: Observable<TokenResponse> =
      this.http.post<TokenResponse>(this.apiURL, body.toString(), this.httpOptions)
        .pipe(
          catchError(this.handleError)
        ) as Observable<TokenResponse>
    result.subscribe({
      next: data => {
        this.accessToken = data
        console.log("accessToken: ", this.accessToken)
      },
      error: error => errorMsg = 'Error reading data from server' + error.message
    })
        // .then(response => this.accessToken = response)
        // .catch(error => console.error('Error: ', error))

    console.log("server response: ", result)
    console.log(errorMsg)

    return result
  }
}
