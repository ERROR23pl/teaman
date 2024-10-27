import {Component, Input} from '@angular/core';
import {NgIf} from '@angular/common';

@Component({
  selector: 'app-signup-form',
  standalone: true,
  imports: [
    NgIf
  ],
  templateUrl: './signup-page.component.html',
  styleUrl: './signup-page.component.css'
})
export class SignupPageComponent {
  @Input() errorMessage = "signup error"
  @Input() isValid: Boolean = true
}
