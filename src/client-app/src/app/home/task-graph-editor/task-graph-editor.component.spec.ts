import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TaskGraphEditorComponent } from './task-graph-editor.component';

describe('TaskGraphEditorComponent', () => {
  let component: TaskGraphEditorComponent;
  let fixture: ComponentFixture<TaskGraphEditorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TaskGraphEditorComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TaskGraphEditorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
