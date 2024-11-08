import {Component, OnInit} from '@angular/core';
import {Router, RouterOutlet} from "@angular/router";
import {AuthGuard} from '../auth.guard';
import {SigninComponent} from '../signin/signin.component';

@Component({
  selector: 'app-welcome-screen',
  standalone: true,
  imports: [
    RouterOutlet,
  ],
  templateUrl: './welcome-screen.component.html',
  styleUrl: './welcome-screen.component.css'
})
export class WelcomeScreenComponent implements OnInit {
  constructor(
    private router: Router,
    protected authGuard: AuthGuard) {}

  ngOnInit() {
    this.authGuard.canActivate().subscribe()
    console.log("welcome screen initialized")
  }
}
