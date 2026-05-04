Feature: Alice high-risk data-loss user journeys
  Alice users need destructive navigation, template/gallery use, legacy migration,
  and Java-transition generation to preserve the work they can still observe. These
  scenarios intentionally extend the save-load/export recovery contract without
  restating archive entry details, backup ordering, or player export structure.

  Background:
    Given Alice has a valid current project named "My Story"
    And the current project has a last-saved checkpoint

  @dirty-session @new-project @data-loss
  Scenario: Canceling a new-project request preserves unsaved work
    Given the current project has an unsaved scene edit named "move bunny forward"
    When the user requests a new blank project
    And the user cancels the unsaved-work decision
    Then Alice keeps "My Story" as the current project
    And the unsaved scene edit "move bunny forward" is still present
    And no new blank project replaces the current project
    And Alice does not write a partial replacement project file

  @dirty-session @open-project @data-loss
  Scenario: Saving succeeds before another project replaces the editor state
    Given the current project has an unsaved scene edit named "add moon prop"
    And "Other Story.a3p" is a readable project archive
    When the user requests to open "Other Story.a3p"
    And the user chooses to save the current project before opening another project
    And saving the current project succeeds
    Then the last-saved checkpoint for "My Story" includes "add moon prop"
    And Alice opens "Other Story.a3p" as the current project
    And Alice does not report a recovery or new-project outcome for "My Story"

  @dirty-session @open-project @save-failure @data-loss
  Scenario: Failed save blocks project replacement
    Given the current project has an unsaved scene edit named "change camera path"
    And "Other Story.a3p" is a readable project archive
    When the user requests to open "Other Story.a3p"
    And the user chooses to save the current project before opening another project
    And saving the current project fails with "disk full"
    Then Alice reports that the current project could not be saved
    And Alice keeps "My Story" as the current project
    And the unsaved scene edit "change camera path" is still present
    And "Other Story.a3p" is not loaded over the current editor state

  @dirty-session @quit @discard @data-loss
  Scenario: Discarding unsaved work closes only the in-memory edits
    Given the current project has an unsaved scene edit named "temporary camera experiment"
    When the user requests to quit Alice
    And the user chooses to discard unsaved work
    Then Alice may close the editor session
    But the last-saved checkpoint for "My Story" is unchanged
    And Alice does not create a corrupted or half-written project file

  @template @data-loss
  Scenario: Editing a project created from a template does not mutate the template
    Given Alice has a project template named "Starter Chase"
    When the user creates a new project from template "Starter Chase"
    And the user changes the new project scene
    And the user saves the new project as "Chase Remix.a3p"
    Then "Chase Remix.a3p" contains the user's scene change
    And template "Starter Chase" remains unchanged for the next project
    And creating another project from "Starter Chase" starts from the original template state

  @gallery @resource @data-loss
  Scenario: Scene edits cannot delete or corrupt the gallery source model
    Given Alice has a gallery model named "Bunny"
    When the user adds gallery model "Bunny" to the current project
    And the user renames and deletes the project scene instance of "Bunny"
    Then the project scene no longer contains that instance
    But gallery model "Bunny" remains available for other projects
    And the gallery model source metadata is unchanged

  @gallery @resource @failure @data-loss
  Scenario: Missing gallery media does not partially replace the current scene
    Given the current project has a scene object named "Bunny"
    And gallery model "Dragon" has missing or restricted media
    When the user attempts to add gallery model "Dragon" to the current project
    Then Alice reports that gallery model "Dragon" could not be loaded
    And the existing scene object "Bunny" is still present
    And Alice does not add a broken placeholder object to the current scene

  @migration @legacy-project @data-loss
  Scenario: Legacy migration failure preserves the original project and current editor state
    Given "Legacy Story.a3p" requires project migration before editing
    And the current project has an unsaved scene edit named "keep current work"
    When the user requests to open "Legacy Story.a3p"
    And migration of "Legacy Story.a3p" fails before a valid migrated project is built
    Then Alice reports that "Legacy Story.a3p" could not be migrated
    And the original "Legacy Story.a3p" file is unchanged
    And Alice keeps "My Story" as the current project
    And the unsaved scene edit "keep current work" is still present

  @migration @legacy-project @data-loss
  Scenario: Migrated legacy projects do not overwrite the original until explicit save
    Given "Legacy Story.a3p" requires project migration before editing
    When Alice opens "Legacy Story.a3p" through a successful migration
    Then Alice shows the migrated project as editable
    And the original "Legacy Story.a3p" file is unchanged
    And Alice marks the migrated editor state as needing an explicit save or save-as decision

  @netbeans-transition @generation @data-loss
  Scenario: Java-transition generation does not delete hand-authored destination files
    Given the user has a NetBeans destination directory containing "Notes.java"
    And Alice can generate Java-transition source for "My Story"
    When the user exports Java-transition project files into that destination
    Then generated Alice source files are written only to the agreed generated locations
    And "Notes.java" is still present with its previous content
    And Alice reports any destination conflict before overwriting a user-authored file
