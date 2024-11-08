import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';
import {Observable, tap, throwError} from 'rxjs';
import { AuthService } from './auth.service';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {
  constructor(
    private authService: AuthService,
    private router: Router
  ) {}

  canActivate(): Observable<boolean> {
    return this.authService.isAuthenticated().pipe(
      tap(isAuthenticated => {
        console.log("from canActivate(), isAuthED = ", isAuthenticated)
        if (!isAuthenticated && !this.router.url.startsWith("/signing")) {
          console.log("No valid token. Navigating to signing page from ", this.router.url)
          this.router.navigate(['/signing/sign-in']).then(
            success => {
             if(success) {
                console.log("Navigated to sign-in successfully")
              }
              else  {
                throwError(() => new Error('Error occured navigating to sign-in component'));
              }
              return true
            }
          );
        }
      })
    );
  }
}
