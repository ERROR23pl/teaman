import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CustomErrorDialogComponent } from './custom-error-dialog.component';

describe('CustomErrorDialogComponent', () => {
  let component: CustomErrorDialogComponent;
  let fixture: ComponentFixture<CustomErrorDialogComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CustomErrorDialogComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CustomErrorDialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
