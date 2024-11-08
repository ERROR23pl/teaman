import {Component, Inject, OnInit, Output} from '@angular/core';
import {RouterLink} from "@angular/router";
import {NgIf} from '@angular/common';
import {SigninService} from './signin.service';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {UserCustomDimension} from '@angular/cli/src/analytics/analytics-parameters';
import {FormsModule} from '@angular/forms';
import {WelcomeScreenComponent} from '../welcome-screen/welcome-screen.component';


@Component({
  selector: 'app-signin',
  standalone: true,
  imports: [
    RouterLink,
    NgIf,
    FormsModule,
    WelcomeScreenComponent,
  ],
  templateUrl: './signin.component.html',
  styleUrl: './signin.component.css'
})
export class SigninComponent implements OnInit {
  @Output() username: string = ""
  @Output() password: string = ""
  error: string = ""

  constructor(private service: SigninService) {
    console.log("SigninService:", this.service)
  }

  ngOnInit() {
  }

  submitCredentials() {
    this.service.fetchAuthToken({
      grant_type: 'password',
      username: this.username,
      password: this.password,
      scope: "",
      client_id: "",
      client_secret: ""
    })
  }

}
