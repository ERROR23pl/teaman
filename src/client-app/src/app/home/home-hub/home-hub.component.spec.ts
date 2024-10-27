import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HomeHubComponent } from './home-hub.component';

describe('HomeHubComponent', () => {
  let component: HomeHubComponent;
  let fixture: ComponentFixture<HomeHubComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HomeHubComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(HomeHubComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
