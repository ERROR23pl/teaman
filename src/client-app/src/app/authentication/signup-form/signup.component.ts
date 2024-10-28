import {Component, Input} from '@angular/core';
import {NgIf} from '@angular/common';
import {RouterLink} from '@angular/router';
import {WelcomeScreenComponent} from '../welcome-screen/welcome-screen.component';

@Component({
  selector: 'app-signup-form',
  standalone: true,
  imports: [
    NgIf,
    RouterLink,
    WelcomeScreenComponent
  ],
  templateUrl: './signup.component.html',
  styleUrl: './signup.component.css'
})
export class SignupComponent {
  @Input() errorMessage = "signup error"
  @Input() isValid: Boolean = true
}
