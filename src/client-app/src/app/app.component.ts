import { Component } from '@angular/core';
import {NavigationError, Router, RouterOutlet} from '@angular/router';
import {MatDialog} from '@angular/material/dialog';
import {CustomErrorDialogComponent} from './error-dialogs/custom-error-dialog/custom-error-dialog.component';
// import { MatToolbar, MatToolbarRow } from '@angular/material/toolbar';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  constructor(private router: Router, private dialog: MatDialog) {
    this.router.events.subscribe((event) => {
      if (event instanceof NavigationError) {
        this.showErrorDialog(event.error?.message || 'An error occurred during navigation.');
      }
    });
  }

  private showErrorDialog(message: string) {
    this.dialog.open(CustomErrorDialogComponent, {
      data: { message },
    });
  }
}
