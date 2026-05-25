# UC Readiness Review — UC089-094 (Cấp mới GCNĐKĐT - Mẫu A.IV.5)
**Functional / Black-box Test Readiness Template — Re-audit v7**

---

## Feature Brief

Chức năng cho phép các Bộ (Bộ Tư pháp / Bộ Công thương / Ngân hàng Nhà nước VN) lập báo cáo định kỳ quý về tình hình cấp mới GCNĐKĐT/giấy tờ có giá trị tương đương cho NĐT nước ngoài trong lĩnh vực quản lý, theo Mẫu A.IV.5. Báo cáo nộp đơn lẻ (single report form) cho Cục ĐTNN (Bộ Tài chính). Dynamic Table 19 cột, max 500 dòng. Hỗ trợ auto-fill qua API CSDL chuyên ngành — tất cả cột vẫn Editable (user chịu trách nhiệm cuối cùng). Import .xlsx only. Quy trình 3 bước (CMCĐT_BCTK_09). Concurrent edit: Last Write Wins.

---

## Readiness Verdict

| Overall Score | Verdict |
| --- | --- |
| **90.0 / 100** | ✅ **READY** |

Raw: 99/110 → Final: round((99/110)×100, 1) = **90.0/100**

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|---|---|---|---|
| UC089-094 | Cấp mới GCNĐKĐT - Mẫu A.IV.5 | v1.6 | Finalized |

| Author / BA | Approved By | Date Created | Last Updated |
|---|---|---|---|
| yen.le2 | — | 2026-04-23 | 2026-05-18 |

---

## 1. Objective & Scope ✅ (5/5)

Objective rõ ràng. In/Out of scope đầy đủ. Không cho phép nộp trễ hạn. Duyệt ở UC riêng.

---

## 2. Actors & Stakeholders ✅ (10/10)

4 actors: 3 Bộ (Primary) + Cục ĐTNN (Receiver). Phân quyền rõ: mỗi Bộ chỉ thấy báo cáo của mình.

---

## 3. Preconditions & Postconditions ✅ (10/10)

Pre: đăng nhập + kỳ "Trong thời hạn". Post: Nộp → Chờ duyệt + Notification; Lưu nháp → Lưu nháp; Xóa → soft-delete + log.

---

## 4. UI Object Inventory & Mapping ⚡ (12/15)

SRS v1.6 liệt kê đầy đủ: 15 elements danh sách + 4 header fields + 19 cột dynamic table + 5 buttons + dòng Tổng + Footer. Tên cột khớp biểu mẫu chính thức. **Gap:** Không có mockup/wireframe đính kèm → trừ 3 điểm.

---

## 5. Object Attributes & Behavior Definition ⚡ (18/20)

Behavior mô tả chi tiết: API auto-fill (Editable), C8 auto-calc, validate C5≥C8 chỉ khi Nộp, Sort (C3 desc default, persist), Concurrent (Last Write Wins), Empty table rule, Max 500 rows. **Gap:** Filter dropdowns trên danh sách thiếu mô tả instant-filter behavior chi tiết → trừ 2 điểm.

---

## 6. Functional Logic & Workflow Decomposition ✅ (20/20)

Đầy đủ: Xem danh sách (nhóm kỳ, collapse, sort), Lập báo cáo (API flow, partial fill, fail fallback, validate, sort, concurrent), Import (.xlsx, CF_02), Tác vụ bổ trợ (7 actions với điều kiện hiển thị rõ ràng theo CMR_03).

---

## 7. Functional Integration Analysis ✅ (10/10)

API integration, Notification, Lifecycle Log, Import, Concurrent edit — tất cả cross-function impacts được mô tả.

---

## 8. Acceptance Criteria ✅ (10/10)

11 AC (AC1–AC11) bao phủ: Import, API success/partial/fail, Validate C5/C8, Sort, Max rows, Empty table, Concurrent edit. Đầy đủ happy + alternative + exception.

---

## 9. Non-functional Requirements ⚡ (4/5)

Performance (load <3s, import <10s, API timeout 5s), Security (RBAC, audit log), Concurrency (Last Write Wins). **Gap:** Thiếu Browser Compatibility và WCAG → trừ 1 điểm.

---

## Audit Summary

| # | Knowledge Area | Max | Score | Status |
|---|---|---|---|---|
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 10/10 | ✅ |
| 5 | UI Object Inventory & Mapping | 15 | 12/15 | ⚡ |
| 6 | Object Attributes & Behavior | 20 | 18/20 | ⚡ |
| 7 | Functional Logic & Workflow | 20 | 20/20 | ✅ |
| 8 | Functional Integration | 10 | 10/10 | ✅ |
| 9 | Acceptance Criteria | 10 | 10/10 | ✅ |
| 10 | Non-functional Requirements | 5 | 4/5 | ⚡ |
| **Total** | | **110** | **99/110** | **90.0/100** |

---

## Unified Gap & Question Report

| ID | Priority | Ref | Issue | Why It Matters | Status |
|---|---|---|---|---|---|
| G1 | Low | UC089-094 | SRS text-only, không có mockup/wireframe | Không verify pixel-level UI | Open |
| G2 | Low | NFR | Thiếu Browser Compatibility, WCAG | Không cover compatibility testing | Open |
| G3 | Info | CMR_12 vs SRS v1.6 | API fill → Editable (khác CMR_12 Disabled) | Client decision, không phải bug | Resolved |

---

## CMR/CF Conflict Check

| Rule | SRS Reference | Conflict? | Detail |
|---|---|---|---|
| CMR_02 | Concurrent edit | ✅ No conflict | Last Write Wins + Lifecycle Log — đúng CMR_02 |
| CMR_03 | Nút Nộp điều kiện | ✅ No conflict | "Lưu nháp hoặc YC chỉnh sửa" — đúng CMR_03 |
| CMR_04 | Nút Lập/Nhập từ file | ✅ No conflict | Ẩn khi Chưa tới hạn/Qua kỳ — đúng CMR_04 |
| CMR_05 | Validate số | ✅ No conflict | Decimal ≥ 0, max 5dp — đúng CMR_05 |
| CMR_06 | Text fields | ✅ No conflict | Placeholder, max length — đúng CMR_06 |
| CMR_07 | Dropdowns | ✅ No conflict | Multiple-selection + instant filter — đúng CMR_07 |
| CMR_09 | Mã báo cáo | ✅ No conflict | FDI_AIV5_[ID] — đúng prefix FDI cho ĐTNN |
| CMR_12 | API fields | ⚠️ Deviation | SRS ghi Editable, CMR_12 ghi Disabled. **Client confirmed Editable.** |
| CMR_16 | Filter "Tất cả" | ✅ No conflict | Các dropdown filter có tham chiếu CMR_16 |
| CF_01 | Lập báo cáo | ✅ No conflict | Luồng đúng CF_01 |
| CF_08 | Xóa | ✅ No conflict | Chỉ Lưu nháp + chưa từng nộp — đúng CF_08 |

---

## Summary & Recommendation

UC089-094 (SRS v1.6) đạt **90.0/100 — READY**. Tên cột khớp biểu mẫu, 11 AC đầy đủ, API/Sort/Concurrent behavior rõ ràng. CMR/CF references không có conflict nghiêm trọng (chỉ 1 deviation CMR_12 đã được client confirm). Sẵn sàng cho test design.

---

## Change Log

| Version | Date | Author | Summary |
|---|---|---|---|
| v7 | 2026-05-21 | QC Re-audit | Re-audit SRS v1.6. Cập nhật tên cột biểu mẫu, API Editable, Last Write Wins, Decimal 5dp, Sort, 11 AC. Score: 87.3→90.0. |
