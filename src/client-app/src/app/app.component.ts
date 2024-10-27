import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { SignupPageComponent } from './signup/signup-form/signup-page.component';
import { MatToolbar, MatToolbarRow } from '@angular/material/toolbar';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, SignupPageComponent, MatToolbar, MatToolbarRow],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {}
